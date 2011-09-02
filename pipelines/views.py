from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from pipelines.models import Pipeline

@login_required
def show_all(request):

    pipelines = Pipeline.objects.all()

    return render_to_response('pipelines/show_all.html', {'pipelines':pipelines}, RequestContext(request))

@login_required
def execution_log(request):

    return render_to_response('pipelines/execution_log.html', {}, RequestContext(request))
