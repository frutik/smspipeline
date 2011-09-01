from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

#@login_required
def home(request):
    return render_to_response('app/home.html', {}, RequestContext(request))
