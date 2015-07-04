from django.http import HttpResponseRedirect, HttpResponse
from manageApp.models import Users
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


# Create your views here.
