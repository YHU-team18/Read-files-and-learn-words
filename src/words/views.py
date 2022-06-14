from re import template
from django.views.generic import TemplateView, CreateView, ListView, CreateView, UpdateView, DetailView
from .models import Word
from django.urls import reverse_lazy

# Create your views here.

class InputPDF(CreateView):
    # 注意: 仮でCreateViewを親にもつ
    template_name: str = "input_pdf.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning_id")

class Quiz(ListView):
    template_name: str = "quiz.html"
    model = Word

class UpDate(ListView):
    # 実際はListViewにして様々な表示の方法をさせ,その一つ一つにUpdateを実装
    template_name: str = "list.html"
    model = Word

class UpDataI(UpdateView):
    # 一つ一つのUpdate
    template_name: str = "update_i.html"
    model = Word

class AddWords(CreateView):
    template_name: str = "add_word.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning","note")
    success_url = reverse_lazy("menu")

class Detail(DetailView):
    template_name: str = "detail.html"
    model = Word
