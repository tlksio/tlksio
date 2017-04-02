import oauth2 as oauth
from urllib import parse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods
from django.db.models import Count

from talks.models import Talk
from talks.models import Profile

# It's probably a good idea to put your consumer's OAuth token and
# OAuth secret into your project's settings.
consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
client = oauth.Client(consumer)

@require_http_methods(["GET"])
def index(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('index.html')

    latest = Talk.objects.all()[:5]
    popular = Talk.objects.annotate(vote_count=Count('votes')).order_by('-vote_count')[:5]

    context = {
        "user": user,
        "latest": latest,
        "popular": popular,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def about(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('about.html')
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def faq(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('faq.html')
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def contactus(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('contactus.html')
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def terms(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('terms.html')
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def privacy(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('privacy.html')
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def activity(request):
    user = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)

    template = loader.get_template('activity.html')

    latest = Talk.objects.all()[:25]

    context = {
        "user": user,
        "latest": latest,
    }

    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def auth_twitter(request):
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    authenticate_url = 'https://api.twitter.com/oauth/authenticate'

    # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")
    # Step 2. Store the request token in a session for later use.
    data = dict(parse.parse_qsl(content))
    request.session['oauth_token'] = data[b'oauth_token'].decode('UTF-8')
    request.session['oauth_token_secret'] = data[b'oauth_token_secret'].decode('UTF-8')
    # Step 3. Redirect the user to the authentication URL.
    url = "%s?oauth_token=%s" % (authenticate_url, request.session['oauth_token'])
    return HttpResponseRedirect(url)


@require_http_methods(["GET"])
def auth_twitter_callback(request):
    access_token_url = 'https://api.twitter.com/oauth/access_token'

    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['oauth_token'], request.session['oauth_token_secret'])
    token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)

    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        print(content)
        raise Exception("Invalid response from Twitter.")

    data = dict(parse.parse_qsl(content))
    twitter_id = data[b'user_id'].decode('UTF-8')
    screen_name = data[b'screen_name'].decode('UTF-8')

    try:
        obj = User.objects.get(username=screen_name)
    except User.DoesNotExist:
        obj = User(username=screen_name)
        obj.save()

    try:
        pobj = Profile.objects.get(twitter_id=twitter_id)
        pobj.oauth_token = data[b'oauth_token'].decode('UTF-8')
        pobj.oauth_token_secret = data[b'oauth_token_secret'].decode('UTF-8')
        pobj.save()
    except Profile.DoesNotExist:
        pobj = Profile(user=obj)
        pobj.twitter_id = twitter_id
        pobj.oauth_token = data[b'oauth_token'].decode('UTF-8')
        pobj.oauth_token_secret = data[b'oauth_token_secret'].decode('UTF-8')
        # TODO Save bio, avatar, url and email
        #pobj.bio = obj.bio
        #pobj.avatar = obj.avatar
        pobj.save()

    request.session['screen_name'] = screen_name
    request.session['twitter_id'] = twitter_id

    return HttpResponseRedirect("/")


@require_http_methods(["GET"])
def logout(request):
    del request.session['oauth_token']
    del request.session['oauth_token_secret']
    del request.session['screen_name']
    del request.session['twitter_id']
    return HttpResponseRedirect("/")


@require_http_methods(["GET", "POST"])
def settings(request):
    profile = None
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']
        user = User.objects.get(username=screen_name)
        profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        user.email = request.POST['email']
        user.save()
        profile.bio = request.POST['bio']
        profile.save()
        return HttpResponseRedirect("/settings")

    template = loader.get_template('settings.html')
    context = {
        "user": profile.user,
        "profile": profile,
    }

    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    talks = Talk.objects.filter(author=user)
    paginator = Paginator(talks, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    template = loader.get_template('profile.html')

    context = {
        "user": profile.user,
        "profile": profile,
        "posted": items,
    }

    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def profile_upvoted(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    talks = Talk.objects.filter(votes__in=[user])
    paginator = Paginator(talks, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    template = loader.get_template('profile_upvoted.html')

    context = {
        "user": profile.user,
        "profile": profile,
        "upvoted": items,
    }

    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def profile_favorited(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    talks = Talk.objects.filter(favorites__in=[user])
    paginator = Paginator(talks, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    template = loader.get_template('profile_favorited.html')

    context = {
        "user": profile.user,
        "profile": profile,
        "favorited": items,
    }

    return HttpResponse(template.render(context, request))

