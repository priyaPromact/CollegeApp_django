from django.conf.urls import include, url
from django.contrib import admin
from manageApp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'collageapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/hello', views.ApiEndpoint.as_view()),
    url(r'^secret$', views.secret_page, name='secret'),
    url(r'^index$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
]
