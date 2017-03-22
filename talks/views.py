from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from talks.models import Talk
from taggit.models import Tag


def latest(request):
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
        "latest": items,
    }
    return HttpResponse(template.render(context, request))


def popular(request):
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
        "popular": items,
    }
    return HttpResponse(template.render(context, request))


def tag(request, tag_slug):
    template = loader.get_template('tag.html')

    items = Talk.objects.filter(tags__name__in=[tag_slug])[:25]
    tag = Tag.objects.get(slug=tag_slug)

    context = {
        "tag": tag,
        "items": items,
    }
    return HttpResponse(template.render(context, request))