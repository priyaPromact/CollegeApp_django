from django.http import HttpResponseRedirect, HttpResponse
from manageApp.models import Users
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))



# Create your views here.

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)
