from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import simplejson
from settings import GRID_TEMPLATE

from message_template.models import MessageTemplate
from message_template.forms import MessageTemplateForm

@login_required
def show_all(request):

    records = MessageTemplate.objects.filter(owner=request.user).order_by('title')

    grid_template = GRID_TEMPLATE
    full_template = 'message_template/show_all.html'

    #if not request.is_ajax:
    if request.GET.get('ajax'):
        template = grid_template
    else:
        template = full_template

    try:
	columns = records[0].grid_columns
    except:
	columns = None
    
    return render_to_response(template, {'records':records, 'columns':columns, 'grid_template':grid_template}, RequestContext(request))

@login_required
def add(request):

    form_template = 'common/add_form.html'
    form_action = reverse('message_template_add')

    if request.method == 'GET':
        form = MessageTemplateForm()
        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))

    form = MessageTemplateForm(request.POST)

    if not form.is_valid():
        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))

    record = MessageTemplate()
    record.title = request.POST.get('title')
    record.regexp = request.POST.get('regexp')
    record.template = request.POST.get('template')
    record.owner = request.user
    record.save()

    return HttpResponse('')
