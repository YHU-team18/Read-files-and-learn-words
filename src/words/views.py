from re import template
from django.views.generic import TemplateView, CreateView, ListView, CreateView, UpdateView, DetailView
from .models import Word
from django.urls import reverse_lazy
from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

# Create your views here.

class InputPDF(CreateView):
    """
    pdf を読み込む View Class
    """
    # 注意: 仮でCreateViewを親にもつ
    template_name: str = "input_pdf.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning_id")

class SubmitPDF(CreateView):
    """
        PDFを送信すると読み込む View Class
    """

    template_name: str = "submit_pdf.html"
    model = Word
    fields = ("word", "importance", "example_sentence", "meaning_id")

    def post(self, request, *args, **kwargs):
        pdf = self.request.FILES['file']
        print("POST_PDF:", pdf)

        # 受け取ったPDFファイルのセーブ(仮でセーブしている。ただ、過去の分も含めてすべて保存されたままになるため、できれば`InMemoryUploadedFile`のまま扱いたい。)
        # `settings.py`にて、MEDIA_ROOTを指定しているため本処理を削除する際は同時に削除をすることを推奨
        # 保存のために`src/tmp`フォルダを作成しているため、これも同時に削除することを推奨
        path = default_storage.save('input_file.pdf', ContentFile(pdf.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print("PDF_PATH:", tmp_file) # すでにファイルがある場合、ファイルパスが自動生成されるため、パスを取得・加工・表示

        return render(request, self.template_name, context=self.kwargs)

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
