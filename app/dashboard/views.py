from tempfile import tempdir
from warnings import catch_warnings
from django.shortcuts import render, redirect
from django.db import connection
from .models import Atbats, Pitches, PitchData, PitchAnalysisView, PitcherInfo
from django.views.decorators.csrf import csrf_exempt
import time
import MySQLdb



def home(request):
    return render(request, 'dashboard/home.html')

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
    param_type = 'minimum pitch count'
    can_redirect = False

    if request.method == "GET":
        selected_proc = request.GET.get("procedures")

    if selected_proc != None:
        param_type = 'pitch type (code)' if ('pitch' in selected_proc and 'info' not in selected_proc) else param_type

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
    attr_list = [
        'ab_id', 
        'batter_id', 
        'event', 
        'g_id', 
        'inning', 
        'o', 
        'p_score', 
        'p_throws',
        'pitcher_id', 
        'stand', 
        'top'
    ]
    msg = ''
    label = ''
    operation = None
    params = {}
    
    if request.method == "GET":
        operation = request.GET.get("operation")

    if operation != None:
        if operation == 'delete':
            msg = 'Provide the key for the entry to be deleted'
        elif operation == 'update':
            msg = 'Provide attribute values for the entry to be updated'
        else:
            msg = 'Provide attribute values for the entry to be inserted'
        label = 'Operation to be attempted: ' + operation.upper()
    
    if request.method == "POST":
        operation = request.GET.get("operation")
        if operation:
            if operation == 'delete':
                params['ab_id'] = request.POST.get("params")
            elif operation == 'update' or operation == 'insert':
                for attr in attr_list:
                    cur_attr = request.POST.get(attr);
                    params[attr] = cur_attr if (cur_attr != None and cur_attr != '') else 0;

        try:
            if params:
                if operation == 'delete':
                    Atbats.objects.filter(ab_id=params['ab_id']).delete()
                elif operation == 'update':
                    obj, created = Atbats.objects.update_or_create(
                        ab_id=params['ab_id'],
                        defaults = {
                            'ab_id':params['ab_id'],
                            'batter_id':params['batter_id'],
                            'event':params['event'],
                            'g_id':params['g_id'],
                            'inning':params['inning'],
                            'o':params['o'],
                            'p_score':params['p_score'],
                            'p_throws':params['p_throws'],
                            'pitcher_id':params['pitcher_id'],
                            'stand':params['stand'],
                            'top':params['top']
                        }
                    )
                    obj.save() if obj else created.save();
                    
                elif operation == 'insert':
                    new_ab = Atbats.objects.create(
                        ab_id=params['ab_id'],
                        batter_id=params['batter_id'],
                        event=params['event'],
                        g_id=params['g_id'],
                        inning=params['inning'],
                        o=params['o'],
                        p_score=params['p_score'],
                        p_throws=params['p_throws'],
                        pitcher_id=params['pitcher_id'],
                        stand=params['stand'],
                        top=params['top'],
                    )
                    new_ab.save()
        except (MySQLdb.Error) as e:
            print(e)
            msg = 'Could not perform ' + operation.upper() + ' for this table entry!'
            label = 'AN ERROR OCCURRED'
            return render(request, 'dashboard/dml.html', {'alert_flag': True, 'success_flag': False, 'error': e})
        except:
            msg = 'Could not perform ' + operation.upper() + ' for this table entry!'
            label = 'AN ERROR OCCURRED'

        if label == 'AN ERROR OCCURRED':
            return render(request, 'dashboard/dml.html', {'alert_flag': True, 'success_flag': False})
        else:
            return render(request, 'dashboard/dml.html', {'alert_flag': True, 'success_flag': True})
    
    context = {
        'attr_list': attr_list,
        'operation': operation,
        'operation_msg': operation.title() + ' a table entry' if operation != None else '',
        'msg': msg,
        'params': params,
        'label': label,
        'alert_flag': False,
        'success_flag': False,
        'error': None
    };
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

@csrf_exempt
def pitch_search(request):
    pitcher_name = None
    view_type = None
    show_table = False
    show_form = True

    if request.method == "POST":
        pitcher_name = request.POST.get("pitcher_name")
        view_type = request.POST.get("view_type")
        return redirect ('pitch_search_detail', pitcher_name=pitcher_name, view_type=view_type, page_num=0)

    context = {
        'pitcher_name': pitcher_name,
        'view_type': view_type,
        'view_type_formatted': view_type.replace("_", " ").title() if view_type else '',
        'show_form': show_form,
        'show_table': show_table
    }
    return render(request, 'dashboard/pitchsearch.html', context)

@csrf_exempt
def pitch_search_detail(request, pitcher_name, view_type, page_num):
    start_index = page_num * 50
    end_index = start_index + 50
    show_form = False
    show_table = True

    if view_type == 'pitch_stats':
        table_data = PitcherInfo.objects.filter(pitcher_name=pitcher_name)
        attr_list = [
            'pitcher_name',
            'avg_start_speed',
            'avg_spin_rate',
            'avg_break_length',
            'avg_break_y'
        ]
    elif view_type == 'all_pitch_data':    
        table_data = PitchAnalysisView.objects.filter(pitcher_name=pitcher_name)[start_index:end_index]
        for data in table_data:
            print('Data: ', data.id, '\n')
        attr_list = [
            'pitcher_name', 'id', 'ab_id', 'batter_id', 
            'batter_name', 'event', 'pitcher_id', 'stand', 
            'top', 'px', 'pz', 'start_speed', 'end_speed', 
            'spin_rate', 'spin_dir', 'break_angle', 'break_length', 
            'break_y', 'nasty', 'zone', 'code', 'type', 'pitch_type'
        ]
    else:
        table_data = []
        attr_list = []
        
    context = {
        'pitcher_name': pitcher_name,
        'view_type': view_type,
        'view_type_formatted': view_type.replace("_", " ").title() if view_type else '',
        'show_form': show_form,
        'show_table': show_table,
        'table_data': table_data,
        'attr_list': attr_list,
        'page_num': page_num,
        'prev_page': 0 if page_num == 0 else page_num - 1,
        'next_page': page_num + 1,
        'start_index': start_index,
        'end_index': end_index
    }
    return render(request, 'dashboard/pitchsearch.html', context)
