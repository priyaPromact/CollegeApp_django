from django.conf.urls import *
from django.contrib import admin
from manageApp import views
from rest_framework import routers
from manageApp.views import *
from django.views.decorators.csrf import csrf_exempt

user_cat_link_list = views.UserCategoryLinkViewset.as_view({
    'get': 'retrieve',
})

user_cat_link_create = views.UserCategoryLinkViewset.as_view({
    'post': 'create',
})

user_clg_link_list = views.UserCollegeLinkViewset.as_view({
    'get': 'retrieve',
})

user_clg_link_create = views.UserCollegeLinkViewset.as_view({
    'post': 'create',
})

router = routers.DefaultRouter()
router.register(r'collegeappregister', views.Register)
router.register(r'collegeappcatlist', views.CategoryListing)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include(router.urls)),
    url(r'^api/login/$',csrf_exempt(Login.as_view())),
    url(r'^api/refresh/$',csrf_exempt(LoginRefresh.as_view())),
    url(r'^secret$', views.secret_page, name='secret'),
    url(r'^index$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^maincatlist$', views.maincatlist, name='maincatlist'),
    url(r'^catuserlist/(?P<id>[0-9]+)/$', user_cat_link_list, name='user_cat_link_list'),
    url(r'^catusercreate/$', user_cat_link_create, name='user_cat_link_create'),
    url(r'^collegeuserlist/(?P<id>[0-9]+)/$', user_clg_link_list, name='user_clg_link_list'),
    url(r'^collegeusercreate/$', user_clg_link_create, name='user_clg_link_create')
)
