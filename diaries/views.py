from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from diaries.models import Diary, Entry

def index(request):
    entries_list = Entry.objects.order_by('pee')[:5]
    template = loader.get_template('diaries/index.html')
    context = {
        'entries_list': entries_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    d = Diary.objects.create(text = request.text, start_date = timezone.now(), baby = request.baby.id)
    return HttpResponse("ok")

def diary(request, diary_id):
    diary = Diary.objects.get(id = diary_id)
    template = loader.get_template('diaries/index.html')
    context = {
        'diary': diary,
    }
    return HttpResponse(template.render(context, request))
