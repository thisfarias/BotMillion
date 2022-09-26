from django.contrib.auth import authenticate, login as loginProcess, logout
from django.contrib.auth.models import User
from django.conf import settings
import json
import ftplib
import os

ip = '31.170.160.95'
port = 21
username = 'u403612333'
password = 'Hz;gMM&0'

def ftp_save(file, name):
    server = ftplib.FTP()
    server.connect(ip, port)
    server.login(username, password)
    server.cwd('/public_html/botMilionario')
    server.storbinary('STOR {}.json'.format(name), file)
    file.close()
    server.quit()

def load_json(data):
    try:
        data = json.loads(data)
    except: 
        pass
    return data

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

def login_admin(request, data):
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

def get_users(data):
    data = load_json(data)
    email = data['email']
    users = User.objects.all()
    filter = []
    if email != '':
        query = users.filter(email__contains=email)
    else:
        query = users

    for q in query:
        filter.append({
            'username': q.username,
            'email': q.email
        })

    return {
        'status': True,
        'message': 'Usuários encontrado com sucesso!',
        'containers': {
            'users': filter
        }
    }

def create_user(data):
    data = load_json(data)
    username = data['username']
    email = data['email']
    password = data['password']
    is_superuser = False

    if email != '' and password != '':
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_superuser=is_superuser
        )
        user.save()
        status = True
        message = 'Usuário criado com sucesso!'
    else:
        status = False
        message = 'Dados inválidos!'

    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def validate_info(data):
    data = load_json(data)
    key = data['key']
    value = data['value']

    validation = False
    if key == 'username':
        if value != '':
            try:
                User.objects.get(username=value)
            except:
                validation = True
    elif key == 'email':
        if value != '':
            try:
                User.objects.get(email=value)
            except:
                validation = True
    elif key == 'password':
        if value != '':
            validation = True

    return {
        'status': True,
        'message': 'Dados validados com sucesso!',
        'containers': {
            'validation': validation
        }
    }

def delete_users(data):
    data = load_json(data)
    username = data['username']

    try:
        query = User.objects.get(username=username)
        query.delete()
        status = True
        message = 'Usuário removido com sucesso"'
    except:
        status = False
        message = 'Usuário não encontrado!'

    return{
        'status': status,
        'message': message,
        'containers': {}
    }

def configs_save(data):
    data = load_json(data)
    link_buy = data['link_buy']

    dict = {
        'link_buy': link_buy
    }

    path = os.path.join(settings.MEDIA_ROOT, 'json')
    with open(os.path.join(path, 'configs.json'), 'w') as file:
        json.dump(dict, file, indent=4)

    file = open(os.path.join(path, 'configs.json'), 'rb')
    ftp_save(file, 'configs')

    return {
        'status': True,
        'message': 'Configurações salvas com sucesso!',
        'containers': {}
    }


