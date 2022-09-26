
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/login', views.login_admin, name='login'),
    path('api/logout', views.logout_admin, name='logout'),
    path('users', views.users, name='users'),
    path('api/users', views.get_users, name='get_users'),
    path('api/users/create', views.create_user, name='create_user'),
    path('api/users/validate/info', views.validate_info, name='create_user'),
    path('api/users/delete', views.delete_users, name='delete_users'),
    path('control', views.control, name='control'),
    path('api/control/save', views.save_control, name='save_control'),
]
