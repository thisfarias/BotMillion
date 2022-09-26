from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from . import controller
from client import controller as client_controller

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'indexAdmin/index.html')
        else:
            return redirect('/')
    else:
        return render(request, 'indexAdmin/login.html')

@csrf_exempt
def login_admin(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.login_admin(request, data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

def logout_admin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/panel')
    else:
        response = controller.not_logged()
        return JsonResponse(response)

def users(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'indexAdmin/apps/users.html')
        else:
            return redirect('/')
    else:
        return redirect('/panel')

@csrf_exempt
def get_users(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data = request.body.decode('utf-8')
                response = controller.get_users(data)
                return render(request, 'indexAdmin/apps/query.html', {
                    'users': response['containers']['users']
                })
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário não autorizado',
                    'containers':{}
                })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Usuário não autorizado',
                'containers':{}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data = request.body.decode('utf-8')
                response = controller.create_user(data)
                return JsonResponse(response)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário não autorizado',
                    'containers':{}
                })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Você não está logado!',
                'containers':{}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def validate_info(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data = request.body.decode('utf-8')
                response = controller.validate_info(data)
                return JsonResponse(response)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário não autorizado',
                    'containers':{}
                })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Você não está logado!',
                'containers':{}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def delete_users(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data = request.body.decode('utf-8')
                response = controller.delete_users(data)
                return JsonResponse(response)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário não autorizado',
                    'containers':{}
                })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Você não está logado!',
                'containers':{}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

def control(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            response = client_controller.configs_get()
            if response['status']:
                configs = response['containers']['configs']
            else:
                configs = {}
            return render(request, 'indexAdmin/apps/control.html', {
                'configs': configs
            })
        else:
            return redirect('/')
    else:
        return redirect('/panel')

@csrf_exempt
def save_control(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data = request.body.decode('utf-8')
                response = controller.configs_save(data)
                return JsonResponse(response)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário não autorizado',
                    'containers':{}
                })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Você não está logado!',
                'containers':{}
            })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)