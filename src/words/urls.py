from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from .views import Menu

urlpatterns = [
    path('menu/', TemplateView.as_view(template_name='menu.html'), name = "menu"),
]
