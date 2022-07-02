from django import template

register = template.Library()

class CFG:
    main_title = "LEAVE🌱"
    title = "最高の英語学習がここにある"
    subtitle = "Improve your English skill"

    author = "Box men"
    home = "HOME"
    pdf = "Input"
    review = "Review"

    menu_title_tag = "HOME"
    input_title_tag = "INPUT"

    input_pdf = "🗂 Input PDF"
    expla_input_pdf = "You can make us read and analyze a file and create Quiz and DataBase for only you."
    quiz = '✔ Quiz'
    exp_quiz = 'You can try some Quiz (word, translate, listening, etc.).'
    add_word = '🔠 Add a New Word'
    add_exp = 'You can add words to DB not via PDF but manually.'
    view_db = '👀 View Your Data Base'
    view_exp = 'You can view and update words\' information.'

    pdf_alert = "下からファイルを追加することができます."
    exp_d_and_d = "ここにドラッグ&ドロップしてください."

    exp_pdf_1 = "今から解析するPDFのIDは 『"
    exp_pdf_2 = "』です.\n 検索の際に絞り込み検索を行えます."
    exp_pdf_3 = "※ 読み込みの関係上,結果を見るためには,ページ移動後に再度読み込む必要がある可能性があります. ※"

    quiz_title_tag = "Quiz"


@register.simple_tag
def call_string(str):
    return getattr(CFG, str)
