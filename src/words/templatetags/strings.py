from django import template

register = template.Library()

class CFG:
    main_title = "LEAVEð±"
    title = "æé«ã®è±èªå­¦ç¿ãããã«ãã"
    subtitle = "Improve your English skill"

    author = "Box men"
    home = "HOME"
    pdf = "Input"
    review = "Review"

    menu_title_tag = "HOME"
    input_title_tag = "INPUT"

    input_pdf = "ð Input PDF"
    expla_input_pdf = "You can make us read and analyze a file and create Quiz and DataBase for only you."
    quiz = 'â Quiz'
    exp_quiz = 'You can try some Quiz (word, translate, listening, etc.).'
    add_word = 'ð  Add a New Word'
    add_exp = 'You can add words to DB not via PDF but manually.'
    view_db = 'ð View Your Data Base'
    view_exp = 'You can view and update words\' information.'

    pdf_alert = "ä¸ãããã¡ã¤ã«ãè¿½å ãããã¨ãã§ãã¾ã."
    exp_d_and_d = "ããã«ãã©ãã°&ãã­ãããã¦ãã ãã."

    exp_pdf_1 = "ä»ããè§£æããPDFã®IDã¯ ã"
    exp_pdf_2 = "ãã§ã.\n æ¤ç´¢ã®éã«çµãè¾¼ã¿æ¤ç´¢ãè¡ãã¾ã."
    exp_pdf_3 = "â» èª­ã¿è¾¼ã¿ã®é¢ä¿ä¸,çµæãè¦ãããã«ã¯,ãã¼ã¸ç§»åå¾ã«ååº¦èª­ã¿è¾¼ãå¿è¦ãããå¯è½æ§ãããã¾ã. â»"

    quiz_title_tag = "Quiz"


@register.simple_tag
def call_string(str):
    return getattr(CFG, str)
