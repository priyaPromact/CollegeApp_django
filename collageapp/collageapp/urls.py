from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'collageapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^manageApp/', include('manageApp.urls')),
    #Admin Urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

]
