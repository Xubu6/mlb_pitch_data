from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from .models import Atbats, Pitches, PitchData

# Create your views here.

def home(request):
    with connection.cursor() as cursor:
        cursor.callproc('spin_rate_leaderboard', ['CU', 200])
    sp_data = cursor.fetchall();
    context = {}
    return render(request, 'dashboard/home.html', context)

def sp(request, sp_name):
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, [100])
    sp_data = cursor.fetchall()[:50];
    context = {
        'sp_data': sp_data,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name.replace("_", " ").title()
    }
    return render(request, 'dashboard/sp.html', context)

def sp_detail(request, page_num, sp_name):
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, [100])
    start_index = page_num * 50
    end_index = start_index + 50
    sp_data = cursor.fetchall()[start_index:end_index];
    context = {
        'sp_data': sp_data,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name.replace("_", " ").title()
    }
    return render(request, 'dashboard/sp.html', context)

def all_data(request):
    pitch_data = PitchData.objects.all()[:50]
    context = {'pitch_data': pitch_data}
    return render(request, 'dashboard/all_data.html', context)

def all_data_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    pitch_data = PitchData.objects.all()[start_index:end_index]
    context = {'pitch_data': pitch_data}
    return render(request, 'dashboard/all_data.html', context)

def atbats(request):
    at_bats = Atbats.objects.all()[:50]
    context = {'at_bats': at_bats}
    return render(request, 'dashboard/atbats.html', context)

def atbats_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    at_bats = Atbats.objects.all()[start_index:end_index]
    context = {'at_bats': at_bats}
    return render(request, 'dashboard/atbats.html', context)

def pitches(request):
    pitches = Pitches.objects.all()[:50]
    context = {'pitches': pitches}
    return render(request, 'dashboard/pitches.html', context)

def pitches_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    pitches = Pitches.objects.all()[start_index:end_index]
    context = {'pitches': pitches}
    return render(request, 'dashboard/pitches.html', context)

def pitches(request):
    pitches = Pitches.objects.all()[:50]
    context = {'pitches': pitches}
    return render(request, 'dashboard/pitches.html', context)

def pitches_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    pitches = Pitches.objects.all()[start_index:end_index]
    context = {'pitches': pitches}
    return render(request, 'dashboard/pitches.html', context)
