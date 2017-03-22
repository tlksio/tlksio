from django.http import HttpResponse
from django.template import loader

from talks.models import Talk


def latest(request):
    template = loader.get_template('latest.html')

    items = Talk.objects.all()[:25]

    context = {
        "latest": items,
    }
    return HttpResponse(template.render(context, request))


def popular(request):
    template = loader.get_template('popular.html')

    items = Talk.objects.order_by('-vote_count')[:25]

    context = {
        "popular": items,
    }
    return HttpResponse(template.render(context, request))

def tag(request):
    template = loader.get_template('latest.html')

    items = Talk.objects.all()[:25]

    context = {
        "latest": items,
    }
    return HttpResponse(template.render(context, request))