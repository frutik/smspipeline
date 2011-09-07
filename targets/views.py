from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.core.urlresolvers import reverse
import simplejson
from settings import GRID_TEMPLATE

from targets.models import Target
from targets.forms import MailTargetForm, TwitterTargetForm

@login_required
def show_all(request):

    records = Target.objects.filter(owner=request.user).order_by('title')

    grid_template = GRID_TEMPLATE
    full_template = 'targets/show_all.html'

    #if not request.is_ajax:
    if request.GET.get('ajax'):
        template = grid_template
    else:
        template = full_template

    context = {
        'records':records,
        'grid_template':grid_template
    }

    if records:
        context['columns'] = records[0].grid_columns
    else:
        context['columns'] = []

    context['empty_list_message'] = 'You haven\'t configured targets.'

    #if Pipeline.__dict__.has_key('enabled'):
    context['could_be_disabled'] = True

    return render_to_response(template, context, RequestContext(request))

@login_required
def add(request):

    form_template = 'common/add_form.html'
    form_action = reverse('pipelines_add')

    if request.method == 'GET':
        form = PipelineForm()
        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))
#
#    form = PipelineForm(request.POST)
#
#    if not form.is_valid():
#        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))

#    record = MessageTemplate()
#    record.title = request.POST.get('title')
#    record.regexp = request.POST.get('regexp')
#    record.template = request.POST.get('template')
#    record.owner = request.user
#    record.save()

    return HttpResponse('')

def set_enabled_many(ids, state):
    records = Target.objects.in_bulk(map(int,ids))
    for k,record in records.items():
        record.enabled = state
        record.save()
    return HttpResponse('')

def enable_many(ids):
    return set_enabled_many(ids, True)

def disable_many(ids):
    return set_enabled_many(ids, False)

def delete_many(ids):
    return HttpResponse('')

MASS_ACTION_HANDLER = {
    'delete_many': delete_many,
    'enable_many': enable_many,
    'disable_many': disable_many,
}

@login_required
def change_many(request):
    return MASS_ACTION_HANDLER[str(request.POST.get('action'))](request.POST.getlist('record_id'))
