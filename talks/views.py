from django.http import HttpResponse
from django.template import loader

from talks.models import Talk


def latest(request):
    template = loader.get_template('latest.html')

    latest = Talk.objects.all()[:25]

    context = {
        "latest": latest,
    }
    return HttpResponse(template.render(context, request))


def popular(request):
    template = loader.get_template('popular.html')

    popular = Talk.objects.order_by('vote_count')[:25]

    context = {
        "popular": popular,
    }
    return HttpResponse(template.render(context, request))