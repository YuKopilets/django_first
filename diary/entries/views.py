from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Entry
import datetime


def index(request):
    entries = Entry.objects.all()
    return render(request, 'entries/entries.html', {'entries': entries})


def save(request):
    text = request.POST['entry_text']
    date = datetime.datetime.today()
    Entry.objects.create(entry_text=text, entry_date=date)
    return HttpResponseRedirect(reverse('entries:index'))
