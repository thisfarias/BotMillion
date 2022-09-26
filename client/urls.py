
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/login', views.api_login, name='api_login'),
    path('api/logout', views.api_logout, name='api_logout'),
    path('logout', views.api_logout, name='api_logout'),
    path('api/entry', views.generate_entry, name='generate_entry'),
    path('lp', views.lp, name='lp'),
]