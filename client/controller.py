from django.contrib.auth import authenticate, login as loginProcess, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.conf import settings
import json
import random
import requests

host = 'engenbot.com'

def load_json(data):
    return json.loads(data)

def method_not_allowed():
    return {
        'status': False,
        'message': 'Método não autorizado!',
        'containers': {}
    }

def not_logged():
    return {
        'status': False,
        'message': 'Usuário não logado!',
        'containers': {}
    }

def api_login(request, data):
    data = load_json(data)
    email = data['email']
    password = data['password']

    try:
        username = User.objects.get(email=email).username
    except:
        username = ''

    if username != '' and password != '':
        user = authenticate(username=username, password=password)
        if user is not None:
            delete_session(username)
            loginProcess(request, user)
            status = True
            message = 'Login realizado com sucesso!'
        else:
            status = False
            message = 'Autenticação inválida!'
    else:
        status = False
        message = 'Dados inválidos!'

    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def generate_entry():
    color = random.choice(['red', 'black'])
    color_pt = 'Vermelho' if color == 'red' else 'Preto'
    percent = random.randint(65, 80)
    return {
        'status': True,
        'message': 'Entrada confirmada com sucesso!',
        'containers': {
            'color': color,
            'color_pt': color_pt,
            'percent': percent,
            'percent_other': 100 - percent,
            'color_other': 'black' if color == 'red' else 'red'
        }
    }

def delete_session(username):
    sessions = Session.objects.all()
    for s in sessions:
        session_decode = s.get_decoded()
        query = User.objects.get(username=username)
        id = query.id
        if int(session_decode['_auth_user_id']) == int(id):
            s.delete()


    return {
        'status': True,
        'message': 'Sessões removidas com sucesso!',
        'containers': {}
    }

def configs_get():
    response = requests.get('http://{}/botMilionario/configs.json'.format(host))
    if response.status_code == 200:
        status = True
        message = 'Configurações recuperadas com sucesso!'
        containers = {
            'configs': response.json()
        }
    else:
        status = False
        message = 'Erro ao recuperar configurações!'
        containers = {}

    return{
        'status': status,
        'message': message,
        'containers': containers
    }
