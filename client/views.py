from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import controller
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
def index(request):
    response = controller.configs_get()
    if response['status']:
        configs = response['containers']['configs']
    else:
        configs = {}
    if request.user.is_authenticated:
        start = request.user.date_joined.date()
        calc = start + datetime.timedelta(days=7)
        today = datetime.datetime.now().date()
        percent = 100 if calc >= today else 99
        return render(request, 'index/index.html', {
            'user': request.user,
            'percent': percent
        })
    else:
        return render(request, 'index/login.html', {
            'configs': configs
        })

@csrf_exempt
def api_login(request):
    if request.method  == 'POST':
        if not request.user.is_authenticated:
            data = request.body.decode('utf-8')
            response = controller.api_login(request, data)
            return JsonResponse(response)
        else:
            return JsonResponse({
                'status': False,
                'message': 'Usuário já logado!',
                'containers': {}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

def api_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        response = controller.not_logged()
        return JsonResponse(response)

@csrf_exempt
def generate_entry(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            response = controller.generate_entry()
            return render(request, 'index/entry.html', {
                'entry': response['containers']
            })
        else:
            response = controller.not_logged()
            return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
        

def lp(request):
    response = controller.configs_get()
    if response['status']:
        configs = response['containers']['configs']
    else:
        configs = {}
    return render(request, 'lp/index.html', {
        'configs': configs
    })