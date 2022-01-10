from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import URL
def index(request):
    return HttpResponse("a")

def redirect(request,short):
    try:
        url_long = URL.objects.get(url_short=short).url_text
    except URL.DoesNotExist:
        return HttpResponseRedirect(reverse('urls:index')) # redirect a new
    return HttpResponseRedirect(url_long)

#class DetailView(generic.DetailView):
#    model = URL
#    template_name = 'URL/detail.html'
#