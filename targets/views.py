from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from targets.models import Target

@login_required
def show_all(request):

    targets = Target.objects.all()

    return render_to_response('targets/show_all.html', {'targets':targets}, RequestContext(request))
