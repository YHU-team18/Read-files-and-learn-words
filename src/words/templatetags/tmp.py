import sys
import os

import django
from django import template
from subprocess import run

pdf_path = "tmp/input_file.pdf"

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yhu_t18.settings')
    
register = template.Library()  

@register.simple_tag
def my_tag():
    a = "Hello!!!"
    django.setup()
    from ..models import Word
    from ...PDFtoBow import PDFtoBoW

    ## ここでfor文を回して追加していく + 論文のIDを付与する

    word = Word(word="Coffee",
                    importance = 100,#np.random.randint(100),
                    example_sentence = "I was told that coffee is bad for you, but it's not so bad if you drink the right amount.",
                    meaning = "珈琲",
                    note = "コーヒーは美味しいよね"
                    )
    word.save()

    run(f"rm -rf {pdf_path}",shell=True)

    return f"{a} {word.word} from tmp() in pyfiles"

