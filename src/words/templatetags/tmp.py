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
    a = "Hello!!!"
    django.setup()
    from ..models import Word
    # from .PDFtoBow import PDFtoBoW
    error = ""
    try:
        from .config import CFG
    except ImportError:
        error = "import error "
        run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {200}' >> {config_path}", shell=True)

    # ## ここでfor文を回して追加していく + 論文のIDを付与する

    word = Word(word="Coffee",
                    importance = 100-CFG.num_thesis ,#np.random.randint(100),
                    example_sentence = "I was told that coffee is bad for you, but it's not so bad if you drink the right amount.",
                    meaning = "珈琲",
                    note = "コーヒーは美味しいよね"
                    )
    word.save()

    if os.path.isfile(config_path):
        run(f"rm {config_path}",shell=True)
    
    run(f"touch {config_path}", shell=True)
    run(f"echo '#論文のidを記録 \nclass CFG:\n    num_thesis = {str(CFG.num_thesis + 1)}' >> {config_path}", shell=True)
    run(f"rm -rf {pdf_path}",shell=True)

    return f"{error}{a} {word.word} {word.importance} from add_sample_data tmp.py in templatetags"
