from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/translate-text', views.translate_text, name='translate_text')
]