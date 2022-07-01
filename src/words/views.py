import os

from re import template

from django.views.generic import TemplateView, CreateView, ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.db.models import Q

from .models import Word

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

        import sys
        from subprocess import run

        import django

        pdf_path = tmp_file #"/code/tmp/input_file.pdf"
        config_path = "/code/words/templatetags/config.py"
        sys.path.append('.')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yhu_t18.settings')

        django.setup()
        from .models import Word
        from .templatetags.PDFtoBow import PDFtoBoW

        error = ""
        try:
            from .templatetags.config import CFG
            from copy import deepcopy
            _CFG = deepcopy(CFG)
        except ImportError:
            error = "import error "
            run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {200}' >> {config_path}", shell=True)
            print("ERROR",error)
            return render(request, self.template_name, context=self.kwargs)

        # ## ここでfor文を回して追加していく + 論文のIDを付与する
        print(_CFG.num_thesis)
        try:
            print("debug: Lemmatization starts")
            print("debug: getcwd()", os.getcwd())
            lemma_list = PDFtoBoW.lemmatization(pdf_path)
            print("debug: Lemmatization finished")
            print("debug: BoW starts")
            bow_dict = PDFtoBoW.get_BoW_using_lemlist(lemma_list)
            print("debug: BoW finished")
            print("debug: ",f"{len(bow_dict)}")
        except FileNotFoundError:
            print("debug: FileNotFoundError")
            # return "There is no file. Please drag and drop pdf-file."
        
        print("debug: Meaning starts")
        mean_dict = PDFtoBoW.get_meaning_using_lemlist(lemma_list)
        print("debug: Meaning finiehed")

        print("debug: phonetics starts")
        phone_dict = PDFtoBoW.get_IPA_from_lemma(lemma_list)
        print("debug: phonetic finiehed")

        print("debug: wiki starts")
        wiki_dict = PDFtoBoW.get_Wikipedia_frequency_from_lemma(lemma_list)
        print("debug: wiki finiehed")

        print("debug:", f"{len(bow_dict)},{len(mean_dict)},{len(phone_dict)},{len(wiki_dict)}")

        if (len(bow_dict) == 0) and (len(mean_dict) == 0):
            if os.path.isfile(pdf_path):
                run(f"rm {pdf_path}",shell=True)
            return "I'm sorry that this pdf file is not readable by me."
        
        for ii, (i,v) in enumerate(bow_dict.items()):
            if not Word.objects.filter(word=i).exists():
                Word.objects.create(word=i,
                            importance = min(100,v) ,#np.random.randint(100),
                            example_sentence = "",
                            meaning = mean_dict[i],
                            note = f"新出論文のIDは{_CFG.num_thesis}-({len(bow_dict)}単語中の{ii}番目の単語として追加.)\n scaled_wiki_freq {int(wiki_dict[i])}",
                            thesis_id = str(_CFG.num_thesis),
                            phonetic = phone_dict[i]
                            )
            if ii==len(bow_dict)-1:
                print("debug: Last stage")
                if os.path.isfile(config_path):
                    run(f"rm {config_path}",shell=True)
                
                run(f"touch {config_path}", shell=True)
                run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {str(_CFG.num_thesis + 1)}' >> {config_path}", shell=True)
                run(f"rm -rf {pdf_path}",shell=True)
                print("debug: rm pdf")

                # return f"(ID: {_CFG.num_thesis}){error}{a} from add_sample_data tmp.py in templatetags"

        return render(request, self.template_name, context=self.kwargs)

class Quiz(ListView):
    """
    Quiz を出題する View Class
    """
    template_name: str = "quiz.html"
    model = Word
    paginate_by: int = 1

class AllList(ListView):
    """
    Quiz でないが 一覧を表示する (アルファベット順)
    """
    # 実際はListViewにして様々な表示の方法をさせ,その一つ一つにUpdateを実装
    template_name: str = "all_list.html"
    model = Word
    paginate_by: int = 5

    def get_queryset(self):
        # Reference: https://noumenon-th.net/programming/2019/12/18/django-search/
        q_word = self.request.GET.get('search')
 
        if q_word:
            object_list = self.model.objects.filter(
                Q(word__startswith=q_word) | Q(thesis_id__iexact=q_word)) # startswith, icontains, exact
        else:
            object_list = self.model.objects.all()
        return object_list

class UpDateI(UpdateView):
    """
    指定されたIDのwordを更新する
    """
    template_name: str = "update_i.html"
    model = Word
    success_url = reverse_lazy("all_list")
    fields = ("word", "meaning", "note", "example_sentence", "importance")

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
