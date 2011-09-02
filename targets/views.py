from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from targets.models import Target
from targets.forms import MailTargetForm, TwitterTargetForm
import simplejson

@login_required
def show_all(request):

    targets = Target.objects.all()

    return render_to_response('targets/show_all.html', {'targets':targets}, RequestContext(request))

@login_required
def add_twitter(request):
    form = MailTargetForm(request.POST)

    if not request.POST:
        return render_to_response('targets/form.html', {'form':form}, RequestContext(request))

    if not form.is_valid():
        html = form.errors.as_ul()
        #response = simplejson.dumps({'success':'False', 'html': html})
        response = html

    else:
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug=slug)
        review.user = request.user
        review.product = product
        review.save()
        template = "catalog/product_review.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})

    return HttpResponse(response)
#    return HttpResponse(response,
#                        content_type='application/javascript; charset=utf-8')
