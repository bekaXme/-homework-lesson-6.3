# adds/url.py

from django.urls import path
from .views import show, first, second, third, fourth, fifth

urlpatterns = [
    path('', show, name='home'),
    path('first/', first, name='first-page'),
    path('second/', second, name='second-page'),
    path('third/', third, name='third-page'),
    path('fourth/', fourth, name='fourth-page'),
    path('fifth/', fifth, name='fifth-page')
]
