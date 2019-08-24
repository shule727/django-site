from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Publication
from django.core.paginator import Paginator, EmptyPage
from django.core import serializers
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError



def index(request):
    sve_objave = Publication.objects.all().values().order_by('-date')
    zadnje_objave = Publication.objects.order_by('-date')[:2]
    sve_objave = list(sve_objave)[2:]



    paginator = Paginator(sve_objave, 1)
    if request.method == 'GET':
        if request.is_ajax():
            if request.GET.get('page_number'):
                # Paginate based on the page number in the GET request
                page_number = request.GET.get('page_number');
                try:
                    page_objects = paginator.page(page_number).object_list
                except EmptyPage:
                    return HttpResponseBadRequest(request)
                # Serialize the paginated objects
                return JsonResponse(page_objects, safe=False)
    sve_objave = paginator.page(1).object_list

    return render(request, 'website/index.html', locals())
def about(request):
    return render(request, 'website/about.html')
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, sender, ['ante.susak@fer.hr'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return confirmation(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {
        'form': form,
    })
def news(request):
    return render(request, 'website/news.html')
def confirmation(request):
    return render(request, 'website/confirmation.html')
def post(request, publication_id):
    publication = Publication.objects.filter(id=publication_id)[0]
    context = {
        'publication': publication
    }

    return render(request, 'website/post.html', locals())
