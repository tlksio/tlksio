from urllib.parse import urlparse
from urllib.parse import parse_qs
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods


from talks.models import Talk
from taggit.models import Tag


@require_http_methods(["GET"])
def latest(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('latest.html')

    talks = Talk.objects.all()
    paginator = Paginator(talks, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        "user": user,
        "latest": items,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def popular(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('popular.html')

    talks = Talk.objects.order_by('-vote_count')
    paginator = Paginator(talks, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        "user": user,
        "popular": items,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def tag(request, tag_slug):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('tag.html')

    items = Talk.objects.filter(tags__slug__in=[tag_slug])[:25]
    tag = Tag.objects.get(slug=tag_slug)

    context = {
        "user": user,
        "tag": tag,
        "items": items,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def talk(request, talk_slug):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('talk.html')

    item = Talk.objects.get(slug=talk_slug)

    context = {
        "user": user,
        "talk": item,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET","POST"])
def add(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    if request.method == 'POST':
        talk = Talk()
        talk.author = user
        talk.title = request.POST['title']
        talk.description = request.POST['description']
        talk.type = 'youtube'
        u = urlparse(request.POST['code'])
        q = parse_qs(u.query)
        talk.code = q['v'][0]
        talk.slug = slugify(talk.title)
        talk.created = datetime.now()
        talk.updated = datetime.now()
        talk.view_count = 0
        talk.vote_count = 0
        talk.fav_count = 0
        talk.save()
        return HttpResponseRedirect('/talk/'+talk.slug)

    template = loader.get_template('add.html')

    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def play(request, talk_slug):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    # TODO : Save when a registered user plays a talk

    item = Talk.objects.get(slug=talk_slug)
    item.view_count = item.view_count + 1
    item.save()
    return HttpResponseRedirect('https://www.youtube.com/watch?v='+item.code)


@require_http_methods(["GET"])
def favorite(request, talk_id):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    item = Talk.objects.get(id=talk_id)
    if item.favorites.filter(id=user.id).count() > 0:
        item.favorites.remove(user)
        item.save()
        return JsonResponse({"favorite": False})
    else:
        item.favorites.add(user)
        item.save()
        return JsonResponse({"favorite": True})


@require_http_methods(["GET"])
def upvote(request, talk_id):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    item = Talk.objects.get(id=talk_id)
    if item.votes.filter(id=user.id).count() == 0:
        item.votes.add(user)
        item.save()
    return JsonResponse({"votes": item.votes.count()})

