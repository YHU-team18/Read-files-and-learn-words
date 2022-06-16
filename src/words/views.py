from re import template
from django.views.generic import TemplateView, CreateView, ListView, CreateView, UpdateView, DetailView
from .models import Word
from django.urls import reverse_lazy

# Create your views here.

class InputPDF(CreateView):
    """
    pdf を読み込む View Class
    """
    # 注意: 仮でCreateViewを親にもつ
    template_name: str = "input_pdf.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning_id")

class Quiz(ListView):
    """
    Quiz を出題する View Class
    """
    template_name: str = "quiz.html"
    model = Word

class AllList(ListView):
    """
    Quiz でないが 一覧を表示する (アルファベット順)
    """
    # 実際はListViewにして様々な表示の方法をさせ,その一つ一つにUpdateを実装
    template_name: str = "all_list.html"
    model = Word

class UpDateI(UpdateView):
    """
    指定されたIDのwordを更新する
    """
    template_name: str = "update_i.html"
    model = Word

class AddWords(CreateView):
    """
    Create
    """
    template_name: str = "add_word.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning","note")
    success_url = reverse_lazy("menu")

class Detail(DetailView):
    """
    指定されたIDの詳細を見れる
    """
    template_name: str = "detail.html"
    model = Word