import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views import ProtectedResourceView
from requests import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from manageApp.models import collegeAppUser, MainCategories, UserCategoryLink
from django.template import RequestContext, loader
from urllib import urlopen
from bs4 import BeautifulSoup, NavigableString
from manageApp.serializers import collegeAppUserSerializer, MainCategorySerializer, UserCategoryLinkSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, generics


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class Register(viewsets.ModelViewSet):
    queryset = collegeAppUser.objects.all()
    serializer_class = collegeAppUserSerializer

    def create(self, request):
        print request.POST
        serializer = collegeAppUserSerializer(data=request.POST)
        print serializer
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors)

class getPreferenceByUser(viewsets.ViewSet):
    queryset = UserCategoryLink.objects.all()
    serializer_class = UserCategoryLinkSerializer

    def create(self, request):
         print request.POST
         data = JSONParser().parse(request)
         queryset = UserCategoryLink.objects.filter(user_id=data.id)
         serializer = UserCategoryLinkSerializer(queryset, many=True)
         return JSONResponse(serializer.data)

class CategoryListing(viewsets.ModelViewSet):
    queryset = MainCategories.objects.all()
    serializer_class = MainCategorySerializer

    def list(self, request):
        queryset = MainCategories.objects.all()
        serializer = MainCategorySerializer(queryset, many=True)
        return JSONResponse(serializer.data)

class UserCategoryLink(viewsets.ModelViewSet):
    queryset = UserCategoryLink.objects.all()
    serializer_class = UserCategoryLinkSerializer

    def create(self, request):
        print request.POST
        serializer = UserCategoryLinkSerializer(data=request.POST)
        print serializer
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors)

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


def home(data):
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
    return JSONResponse(data)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print data
        serializer = collegeAppUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    return JSONResponse('no data', status=400)

@csrf_exempt
def maincatlist(request):
    if request.method == 'GET':
        queryset = MainCategories.objects.all()
        serializer = MainCategorySerializer(queryset, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse('no data', status=400)

@csrf_exempt
def saveusermaincat(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserCategoryLinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    return JSONResponse('no data', status=400)