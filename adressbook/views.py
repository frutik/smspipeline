from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import simplejson
from settings import GRID_TEMPLATE

from adressbook.models import AdressBook
from adressbook.forms import AdressBookForm

@login_required
def show_all(request):

    records = AdressBook.objects.filter(owner=request.user).order_by('title')

    grid_template = GRID_TEMPLATE
    full_template = 'adressbook/show_all.html'

    #if not request.is_ajax:
    if request.GET.get('ajax'):
        template = grid_template
    else:
        template = full_template

    columns = records[0].grid_columns

    return render_to_response(template, {'records':records, 'columns':columns, 'grid_template':grid_template}, RequestContext(request))

@login_required
def add(request):

    form_template = 'common/add_form.html'
    form_action = reverse('adressbook_add')

    if request.method == 'GET':
        form = AdressBookForm()
        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))

    form = AdressBookForm(request.POST)

    if not form.is_valid():
        return render_to_response(form_template, {'form':form, 'action':form_action}, RequestContext(request))

    record = AdressBook()
    record.title = request.POST.get('title')
    record.phone_number = request.POST.get('phone_number')
    record.owner = request.user
    record.save()

    return HttpResponse('')
