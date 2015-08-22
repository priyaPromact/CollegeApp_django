from django.conf.urls import *
from django.contrib import admin
from manageApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'collegeappregister', views.Register)
router.register(r'collegeappcatlist', views.CategoryListing)
router.register(r'collegeappusercatlink', views.UserCategoryLink)
router.register(r'collegeappgetpref', views.getPreferenceByUser)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include(router.urls)),
    url(r'^secret$', views.secret_page, name='secret'),
    url(r'^index$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^maincatlist$', views.maincatlist, name='maincatlist')
)
