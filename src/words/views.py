from django.views.generic import TemplateView, CreateView, ListView, CreateView, UpdateView
from .models import Word

# Create your views here.

class Menu(TemplateView):
    template_name: str = "menu.html"

class InputPDF(CreateView):
    template_name: str = "input_pdf.html"
    model = Word

class Quiz(ListView):
    template_name: str = "quiz.html"
    model = Word

class UpDate(UpdateView):
    template_name: str = "update.html"
    model = Word
