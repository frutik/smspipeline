from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from adressbook.models import AdressBook
from adressbook.forms import AdressBookForm
from django.http import HttpResponseRedirect

@login_required
def show_all(request):

    records = AdressBook.objects.all().order_by('title')

    return render_to_response('adressbook/show_all.html', {'records':records}, RequestContext(request))

@login_required
def add(request):
    form = AdressBookForm(request.POST)

    if not request.POST:
        return render_to_response('adressbook/add_form.html', {'form':form}, RequestContext(request))
#    if request.is_ajax:
#        # response is just the form
#        return render(request, 'contact/fields.html', {'form':form})
#    else:
#        # response is the entire page
#        return render(request, 'contact/form.html', {'form':form})

    if not form.is_valid():
            html = form.errors.as_ul()
            #response = simplejson.dumps({'success':'False', 'html': html})
            response = html

    else:
        adressbook = AdressBook()
        adressbook.title = request.POST.get('title')
        adressbook.phone_number = request.POST.get('phone_number')
        adressbook.owner = request.user
        adressbook.save()

        #TODO: message
        return HttpResponseRedirect('/adressbook/')
#        template = "catalog/product_review.html"
#        html = render_to_string(template, {'review': review })
#        response = simplejson.dumps({'success':'True', 'html': html})

    return HttpResponse(response)
#    return HttpResponse(response,
#                        content_type='application/javascript; charset=utf-8')
