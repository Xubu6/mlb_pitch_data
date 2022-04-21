from tempfile import tempdir
from django.shortcuts import render
from django.db import connection
from .models import Atbats, Pitches, PitchData

# Create your views here.

pitch_types = {
    'CH': 'Changeup',
    'CU': 'Curveball',
    'EP': 'Eephus',
    'FC': 'Cutter',
    'FF': 'Four-seam Fastball',
    'FO': 'Pitchout',
    'FS': 'Splitter',
    'FT': 'Two-seam Fastball',
    'IN': 'Intentional Ball',
    'KC': 'Knuckle Curve',
    'KN': 'Knuckleball',
    'PO': 'Pitchout',
    'SC': 'Screwball',
    'SI': 'Sinker',
    'SL': 'Slider',
    'UN': 'Unknown'
}

def home(request):
    temp_data = {
        'Welcome to the Home Page!',
        'Explore the site!',
        'Play around with our advanced features!'
    }
    context = {
        'temp_data': temp_data
    }
    return render(request, 'dashboard/home.html', context)

def stats(request):
    temp_data = {
        'Welcome to the Advanced Stats Page!',
        'We will eventually have a user input form here where you can try out our different features'
    }
    context = {
        'temp_data': temp_data
    }
    return render(request, 'dashboard/stats.html', context)

def sp(request, sp_name):
    sp_params = ['SL',500]
    start_index = 0
    end_index = 50
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, sp_params)
        sp_data_full = cursor.fetchall();
        total_rows = len(sp_data_full)
        sp_data = sp_data_full[start_index:end_index];
        attr_list = [attr[0] for attr in cursor.description]
        sp_name_formatted = sp_name.replace("_", " ").title() + ' for ' + pitch_types[sp_params[0]] if len(sp_params) > 1 else sp_name.replace("_", " ").title()
    context = {
        'sp_data': sp_data,
        'attr_list': attr_list,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name_formatted,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/sp.html', context)

def sp_detail(request, page_num, sp_name):
    sp_params = ['SL',500]
    start_index = page_num * 50
    end_index = start_index + 50
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, sp_params)
        sp_data_full = cursor.fetchall();
        total_rows = len(sp_data_full)
        sp_data = sp_data_full[start_index:end_index]
        attr_list = [attr[0] for attr in cursor.description]
        sp_name_formatted = sp_name.replace("_", " ").title() + ' — Pitch Type: ' + pitch_types[sp_params[0]] if len(sp_params) > 1 else sp_name.replace("_", " ").title()
    context = {
        'sp_data': sp_data,
        'attr_list': attr_list,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name_formatted,
        'page_num': page_num,
        'prev_page': 0 if page_num == 0 else page_num - 1,
        'next_page': page_num + 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/sp.html', context)

def all_data(request):
    start_index = 0
    end_index = 50
    total_rows = 2867154
    pitch_data = PitchData.objects.all()[start_index:end_index]
    context = {
        'pitch_data': pitch_data,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/all_data.html', context)

def all_data_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    total_rows = 2867154
    pitch_data = PitchData.objects.all()[start_index:end_index]
    context = {
        'pitch_data': pitch_data,
        'page_num': page_num,
        'prev_page': 0 if page_num == 0 else page_num - 1,
        'next_page': page_num + 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/all_data.html', context)

def atbats(request):
    start_index = 0
    end_index = 50
    at_bats = Atbats.objects.all()[start_index:end_index]
    total_rows = 740389
    context = {
        'at_bats': at_bats,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/atbats.html', context)

def atbats_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    at_bats = Atbats.objects.all()[start_index:end_index]
    total_rows = 740389
    context = {
        'at_bats': at_bats,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/atbats.html', context)

def pitches(request):
    start_index = 0
    end_index = 50
    total_rows = 2867154
    pitches = Pitches.objects.all()[start_index:end_index]
    context = {
        'pitches': pitches,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/pitches.html', context)

def pitches_detail(request, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    total_rows = 2867154
    pitches = Pitches.objects.all()[start_index:end_index]
    context = {
        'pitches': pitches,
        'page_num': page_num,
        'prev_page': 0 if page_num == 0 else page_num - 1,
        'next_page': page_num + 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/pitches.html', context)
