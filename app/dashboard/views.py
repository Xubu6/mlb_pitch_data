from tempfile import tempdir
from django.shortcuts import render, redirect
from django.db import connection
from .models import Atbats, Pitches, PitchData
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def stats(request):
    pitch_types = {
        'CH: Changeup',
        'CU: Curveball',
        'EP: Eephus',
        'FC: Cutter',
        'FF: Four-seam Fastball',
        'FO: Pitchout',
        'FS: Splitter',
        'FT: Two-seam Fastball',
        'IN: Intentional Ball',
        'KC: Knuckle Curve',
        'KN: Knuckleball',
        'PO: Pitchout',
        'SC: Screwball',
        'SI: Sinker',
        'SL: Slider',
        'UN: Unknown'
    }
    selected_proc = None
    cur_proc_param = None
    param_type = 'sample size'
    can_redirect = False

    if request.method == "GET":
        selected_proc = request.GET.get("procedures")

    if selected_proc != None:
        param_type = 'pitch type (code)' if ('pitch' in selected_proc and 'info' not in selected_proc) else param_type
        # if cur_proc_param != None:
        #     return redirect ('sp', sp_name=selected_proc, sp_param=cur_proc_param)

    if request.method == "POST":
        selected_proc = request.GET.get("procedures")
        cur_proc_param = request.POST.get("param")
        return redirect ('sp', sp_name=selected_proc, sp_param=cur_proc_param)
        
    if selected_proc != None and cur_proc_param != None:
        can_redirect = True

    context = {
        'sp_name': selected_proc,
        'sp_name_formatted': selected_proc.replace("_", " ").title() if selected_proc != None else '',
        'sp_param': cur_proc_param,
        'pitch_types': pitch_types,
        'param_type': param_type,
        'can_redirect': can_redirect
    }
    return render(request, 'dashboard/stats.html', context)

@csrf_exempt
def dml(request):
    context = {};
    return render(request, 'dashboard/dml.html', context)

@csrf_exempt
def sp(request, sp_name, sp_param):
    sp_params = [sp_param]
    start_index = 0
    end_index = 50
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, sp_params)
        sp_data_full = cursor.fetchall();
        total_rows = len(sp_data_full)
        sp_data = sp_data_full[start_index:end_index];
        attr_list = [attr[0] for attr in cursor.description]
        sp_name_formatted = sp_name.replace("_", " ").title() + ' (' + sp_param + ')'
    context = {
        'sp_data': sp_data,
        'attr_list': attr_list,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name_formatted,
        'sp_param': sp_param,
        'page_num': 0,
        'prev_page': 0,
        'next_page': 1,
        'start_index': start_index,
        'end_index': end_index,
        'total_rows': total_rows
    }
    return render(request, 'dashboard/sp.html', context)

@csrf_exempt
def sp_detail(request, page_num, sp_name, sp_param):
    sp_params = [sp_param]
    start_index = page_num * 50
    end_index = start_index + 50
    with connection.cursor() as cursor:
        cursor.callproc(sp_name, sp_params)
        sp_data_full = cursor.fetchall();
        total_rows = len(sp_data_full)
        sp_data = sp_data_full[start_index:end_index]
        attr_list = [attr[0] for attr in cursor.description]
        sp_name_formatted = sp_name.replace("_", " ").title() + ' (' + sp_param + ')'
    context = {
        'sp_data': sp_data,
        'attr_list': attr_list,
        'sp_name': sp_name,
        'sp_name_formatted': sp_name_formatted,
        'sp_param': sp_param,
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
        'page_num': page_num,
        'prev_page': 0 if page_num == 0 else page_num - 1,
        'next_page': page_num + 1,
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
