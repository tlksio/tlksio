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