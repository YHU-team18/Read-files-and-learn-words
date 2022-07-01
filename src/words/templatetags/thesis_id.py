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
def get_latest_id():
    from .config import CFG
    from copy import deepcopy

    _CFG = deepcopy(CFG)
    return _CFG.num_thesis
