import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from oauth2_provider.views import ProtectedResourceView
from manageApp.models import Users
from django.template import RequestContext, loader
from urllib import urlopen
from bs4 import BeautifulSoup, NavigableString


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


def home(request):
    url = urllib.urlopen("http://www.svitvasad.ac.in/")
    soup = BeautifulSoup(url, "html.parser")
    data = []
    head = ""

    for link in soup.find(id="news"):
        if not isinstance(link, NavigableString):
            if link.name == "h1":
                head = link.string
            for h2 in link.find_all("h2"):
                data.append(h2.string)

    return render(request, "base.html", {'head': head, 'data': data})