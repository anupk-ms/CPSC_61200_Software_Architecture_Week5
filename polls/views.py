from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    #return HttpResponse("{\"Message\": \"Hello world!\"}")
    return JsonResponse({'Message': 'Hello world!'})

def index(request):
	rendered = render_to_string('helloWorld.html')
	return HttpResponse(rendered)
