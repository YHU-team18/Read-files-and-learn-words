from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import InputPDF, Quiz, AllList, UpDateI, AddWords, Detail

urlpatterns = [
    path('menu/', TemplateView.as_view(template_name='menu.html'), name = "menu"),
    path("input_pdf/", InputPDF.as_view(), name = "input_da"),
    path("quiz/", Quiz.as_view(), name = "quiz"),
    path("all_list/", AllList.as_view(), name = "all_list"),
    path("update_i/<int:pk>", UpDateI.as_view(), name = "update_i"), # Generic detail view Detail must be called with either an object pk or a slug in the URLconf.
    path("add_words/", AddWords.as_view(), name = "add_words"),
    path("detail/<int:pk>", Detail.as_view(), name = "detail") # Generic detail view Detail must be called with either an object pk or a slug in the URLconf.
]
