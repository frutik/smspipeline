from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from adressbook.models import AdressBook
from adressbook.forms import AdressBookForm
from django.http import HttpResponseRedirect, HttpResponse
import simplejson

@login_required
def show_all(request):

    records = AdressBook.objects.filter(owner=request.user).order_by('title')

    #if not request.is_ajax:
    if request.GET.get('ajax'):
        template = 'adressbook/show_all_ajax.html'
    else:
        template = 'adressbook/show_all.html'

    return render_to_response(template, {'records':records}, RequestContext(request))

@login_required
def add(request):
    if request.method == 'GET':
        form = AdressBookForm()
        return render_to_response('adressbook/add_form.html', {'form':form}, RequestContext(request))

#    if not request.POST:
#    if request.is_ajax:
#        # response is just the form
#        return render(request, 'contact/fields.html', {'form':form})
#    else:
#        # response is the entire page
#        return render(request, 'contact/form.html', {'form':form})
    form = AdressBookForm(request.POST)

    if not form.is_valid():
        return render_to_response('adressbook/add_form.html', {'form':form}, RequestContext(request))
        return HttpResponse(
            simplejson.dumps({'success':'False', 'errors': form.errors}),
            content_type='application/javascript; charset=utf-8'
        )

    adressbook = AdressBook()
    adressbook.title = request.POST.get('title')
    adressbook.phone_number = request.POST.get('phone_number')
    adressbook.owner = request.user
    adressbook.save()

#    import time
#    time.sleep(30)

    #TODO: message
    return HttpResponse('')
    return HttpResponseRedirect('/adressbook/')
#        template = "catalog/product_review.html"
#        html = render_to_string(template, {'review': review })
#        response = simplejson.dumps({'success':'True', 'html': html})

#    return HttpResponse(response)
#    return HttpResponse(response,
#                        content_type='application/javascript; charset=utf-8')
