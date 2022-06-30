import sys
import os

import django
from django import template
from subprocess import run

pdf_path = "tmp/input_file.pdf"
config_path = "words/templatetags/config.py"

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yhu_t18.settings')
    
register = template.Library()  

@register.simple_tag
def add_sample_data():
    print("debug: add_sample_data() is called")
    a = "Hello!!!"
    django.setup()
    from ..models import Word
    from .PDFtoBow import PDFtoBoW
    error = ""
    try:
        from .config import CFG
    except ImportError:
        error = "import error "
        run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {200}' >> {config_path}", shell=True)

    # ## ここでfor文を回して追加していく + 論文のIDを付与する
    print(CFG.num_thesis)
    try:
        print("debug: Lemmatization starts")
        lemma_list = PDFtoBoW.lemmatization(pdf_path)
        print("debug: Lemmatization finished")
        print("debug: BoW starts")
        bow_dict = PDFtoBoW.get_BoW_using_lemlist(lemma_list)
        print("debug: BoW finished")
        print("debug: ",f"{len(bow_dict)}")
    except FileNotFoundError:
        print("debug: FileNotFoundError")
        return "There is no file. Please drag and drop pdf-file."
    
    print("debug: Meaning starts")
    mean_dict = PDFtoBoW.get_meaning_using_lemlist(lemma_list)
    print("debug: Meaning finiehed")

    print("debug:", f"{len(bow_dict)},{len(mean_dict)}")

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
                        note = f"(新出)論文のIDは{CFG.num_thesis}-{ii}-{len(bow_dict)}-{len(mean_dict)}",
                        thesis_id = CFG.num_thesis
                        )
        if ii==len(bow_dict)-1:
            print("debug: Last stage")
            if os.path.isfile(config_path):
                run(f"rm {config_path}",shell=True)
            
            run(f"touch {config_path}", shell=True)
            run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {str(CFG.num_thesis + 1)}' >> {config_path}", shell=True)
            run(f"rm -rf {pdf_path}",shell=True)
            print("debug: rm pdf")

            return f"(ID: {CFG.num_thesis}){error}{a} from add_sample_data tmp.py in templatetags"
