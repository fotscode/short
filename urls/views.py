from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import URL

def url_formatter(url):
    return url if (url.startswith("https://")) else f"https://{url}"


def index(request):
    return render(request, "urls/index.html")

def redirect(request,short):
    try:
        url_long = URL.objects.get(url_short=short).url_text
    except URL.DoesNotExist:
        return HttpResponseRedirect(reverse('urls:index')) # redirect a index
    return HttpResponseRedirect(url_long)

def new(request):
    short = request.POST["url_short"]
    long = url_formatter(request.POST["url_long"])
    try:
        u = URL.objects.get(url_short=short).url_text
        return render(request,'urls/index.html',{'error_message':'URL already exists'}) # redirect a index
    except URL.DoesNotExist:
        u = URL(url_text=long,url_short=short,pub_date=timezone.now())
        u.save()
    return HttpResponseRedirect(reverse('urls:index'),{'error_mesage':'URL succesfully registered'}) # redirect a index

class DetailView(generic.DetailView):
    model = URL
    template_name = 'urls/detail.html'