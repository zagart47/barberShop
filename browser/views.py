from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import *
from .models import *

menu = [{'title': "Главная страница", 'url_name': 'index'},
        {'title': "Барберы", 'url_name': 'barbers'},
        {'title': "Услуги", 'url_name': 'service'},
        {'title': "Записаться", 'url_name': 'enroll'},
        {'title': "Галерея", 'url_name': 'gallery'},
        {'title': "Контакты", 'url_name': 'contacts'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'browser/index.html', context=context)


def barbers(request):
    barber = Barber.objects.all()
    context = {
        'barber': barber,
        'menu': menu,
        'title': 'Наши барберы'
    }
    return render(request, 'browser/barbers.html', context=context)


def barber_details(request, barber_id):
    barber = Barber.objects.get(pk=barber_id)
    context = {
        'barber': barber,
        'menu': menu,
        'title': barber.barber_name
    }

    if len(barber.barber_name) == 0:
        raise Http404()
    return render(request, 'browser/barberdetails.html', context=context)


def contacts(request):
    return render(request, 'browser/contacts.html')


def enroll(request):
    if request.method == 'POST':
        form = AddVisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = AddVisitForm()

    context = {
        'form': form,
        'menu': menu,
        'title': 'Записаться к барберу'
    }
    return render(request, 'browser/enroll.html', context=context)


def service(request):
    return render(request, 'browser/service.html')


def gallery(request):
    return render(request, 'browser/gallery.html')
