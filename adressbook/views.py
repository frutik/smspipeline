from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from adressbook.models import AdressBook
from adressbook.forms import AdressBookForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import simplejson

@login_required
def show_all(request):

    records = AdressBook.objects.filter(owner=request.user).order_by('title')

    #if not request.is_ajax:
    if request.GET.get('ajax'):
        template = 'adressbook/grid.html'
    else:
        template = 'adressbook/show_all.html'

    return render_to_response(template, {'records':records}, RequestContext(request))

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
        return HttpResponse(
            simplejson.dumps({'success':'False', 'errors': form.errors}),
            content_type='application/javascript; charset=utf-8'
        )

    adressbook = AdressBook()
    adressbook.title = request.POST.get('title')
    adressbook.phone_number = request.POST.get('phone_number')
    adressbook.owner = request.user
    adressbook.save()

    return HttpResponse('')
