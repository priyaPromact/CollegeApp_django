import hashlib
import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views import ProtectedResourceView
from requests import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from manageApp.models import collegeAppUser, MainCategories, UserCategoryLink, CollegeCategoryLink, College, UserCollegeLink
from django.template import RequestContext, loader
from urllib import urlopen
from bs4 import BeautifulSoup, NavigableString
from manageApp.serializers import collegeAppUserSerializer, MainCategorySerializer, UserCategoryLinkSerializer, CollegeCategoryLinkSerializer, CollegeSerializer, UserCollegeLinkSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, generics
from django.views.generic import View


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

class CategoryListing(viewsets.ModelViewSet):
    queryset = MainCategories.objects.all()
    serializer_class = MainCategorySerializer

    def list(self, request):
        queryset = MainCategories.objects.all()
        serializer = MainCategorySerializer(queryset, many=True)
        return JSONResponse(serializer.data)

class UserCategoryLinkViewset(viewsets.ViewSet):
    serializer_class = UserCategoryLinkSerializer

    def create(self, request):
        selectedCats = []
        collegeList = []
        data = JSONParser().parse(request)
        for field in data:
            selectedCats.append(field['cat'])
            ucl = UserCategoryLink()
            ucl.user = collegeAppUser.objects.get(id=field['user'])
            ucl.cat = MainCategories.objects.get(id=field['cat'])
            if not UserCategoryLink.objects.filter(user=field['user'], cat=field['cat']).exists():
                ucl.save()

        for cats in selectedCats:
            queryset = CollegeCategoryLink.objects.filter(category_id=cats)
            serializer = CollegeCategoryLinkSerializer(queryset, many=True)
            for clg in serializer.data:
                queryset_college = College.objects.filter(id=clg['college_id'])
                serializer_college = CollegeSerializer(queryset_college, many=True)
                collegeList.append(serializer_college.data)

        return JSONResponse(collegeList)

    def retrieve(self, request, id):
         print id
         queryset = UserCategoryLink.objects.filter(user_id=id)
         serializer = UserCategoryLinkSerializer(queryset, many=True)
         return JSONResponse(serializer.data)

class UserCollegeLinkViewset(viewsets.ViewSet):
     serializer_class = UserCollegeLinkSerializer

     def create(self, request):
        selectedCollege = []
        collegeData = []
        data = JSONParser().parse(request)
        for field in data:
            selectedCollege.append(field['college'])
            ucl = UserCollegeLink()
            ucl.user = collegeAppUser.objects.get(id=field['user'])
            ucl.college = College.objects.get(id=field['college'])
            if not UserCollegeLink.objects.filter(user=field['user'], college=field['college']).exists():
                ucl.save()

        for clg in selectedCollege:
            queryset = College.objects.filter(id=clg)
            serializer = CollegeSerializer(queryset, many=True)
            collegeData.append(home(serializer.data[0]['college_url']))

        return JSONResponse(collegeData)

     def retrieve(self, request, id):
         print id
         queryset = UserCollegeLink.objects.filter(user_id=id)
         serializer = UserCollegeLinkSerializer(queryset, many=True)
         return JSONResponse(serializer.data)

class Login(View):

    def post(self,request):
        collegeData = []
        data = JSONParser().parse(request)
        querysetUser = collegeAppUser.objects.filter(username=data['username'],password=hashlib.md5(data['password']).hexdigest())
        serializerUser = collegeAppUserSerializer(querysetUser, many=True)
        if serializerUser.data:
           collegesQueryset = UserCollegeLink.objects.filter(user_id=serializerUser.data[0]['id'])
           collegeSerializer = UserCollegeLinkSerializer(collegesQueryset,many=True)
           print collegeSerializer.data[0]
           for clg in collegeSerializer.data:
                print collegeSerializer.data[0]
                queryset = College.objects.filter(id=clg['college'])
                serializer = CollegeSerializer(queryset, many=True)
                collegeData.append({'user':serializerUser.data[0],'college':serializer.data[0],'news':home(serializer.data[0]['college_url'])})
        return JSONResponse(collegeData)


class LoginRefresh(View):

    def post(self,request):
        collegeData = []
        data = JSONParser().parse(request)
        querysetUser = collegeAppUser.objects.filter(id=data['id'])
        serializerUser = collegeAppUserSerializer(querysetUser, many=True)
        if serializerUser.data:
           collegesQueryset = UserCollegeLink.objects.filter(user_id=serializerUser.data[0]['id'])
           collegeSerializer = UserCollegeLinkSerializer(collegesQueryset,many=True)
           print collegeSerializer.data[0]
           for clg in collegeSerializer.data:
                print collegeSerializer.data[0]
                queryset = College.objects.filter(id=clg['college'])
                serializer = CollegeSerializer(queryset, many=True)
                collegeData.append({'user':serializerUser.data[0],'college':serializer.data[0],'news':home(serializer.data[0]['college_url'])})
        return JSONResponse(collegeData)

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
    print data
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
    return data

def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print data

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