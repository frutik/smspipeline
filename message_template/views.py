from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from message_template.models import MessageTemplate

@login_required
def show_all(request):

    templates = MessageTemplate.objects.all()

    return render_to_response('message_template/show_all.html', {'templates':templates}, RequestContext(request))

