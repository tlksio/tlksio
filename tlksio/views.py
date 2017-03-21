from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def faq(request):
    template = loader.get_template('faq.html')
    context = {}
    return HttpResponse(template.render(context, request))


def contactus(request):
    template = loader.get_template('contactus.html')
    context = {}
    return HttpResponse(template.render(context, request))


def terms(request):
    template = loader.get_template('terms.html')
    context = {}
    return HttpResponse(template.render(context, request))


def privacy(request):
    template = loader.get_template('privacy.html')
    context = {}
    return HttpResponse(template.render(context, request))