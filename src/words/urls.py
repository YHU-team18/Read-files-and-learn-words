from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import InputPDF, Quiz, UpDate, AddWords, Detail

urlpatterns = [
    path('menu/', TemplateView.as_view(template_name='menu.html'), name = "menu"),
    path("input_pdf/", InputPDF.as_view(), name = "input_da"),
    path("quiz/", Quiz.as_view(), name = "quiz"),
    path("update_list/", UpDate.as_view(), name = "list"),
    path("update_i/", UpDate.as_view(), name = "update_i"),
    path("add_words", AddWords.as_view(), name = "add_words"),
    path("detail/", Detail.as_view(), name = "detail")
]
