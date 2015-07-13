from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'collageapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^admin/', include(admin.site.urls)),
     url(r'^manageApp/', include('manageApp.urls', namespace="manageApp")),

]
