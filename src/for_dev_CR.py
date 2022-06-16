import sys
import os
import django

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yhu_t18.settings')

def call():
    django.setup()
    from words.models import Word

    objects = Word.objects.all()
    n = len(objects)

    print(f"The size of objects {n}")
    if n < 7:
        for i,obj in enumerate(objects):
            print(i, obj.id, obj, obj.meaning, obj.importance)
    else:
        for i,obj in enumerate(objects):
            if i in [0,1,2,n-3,n-2,n-1]:
                print(i, obj.id, obj, obj.meaning, obj.importance)
                if i ==2:
                    print("...")

def add_default(n):
    django.setup()
    from words.models import Word
    import random # numpyを使うにはDockerfileを編集せよ
    import string

    for _ in range(n):
        top = "".join([random.choice(string.ascii_letters) for _ in range(3)])
        last = "".join([random.choice(string.ascii_letters) for _ in range(3)])
        word = Word(word=f"{top}-hack-{last}",
                    importance = random.randint(0,99),#np.random.randint(100),
                    example_sentence = "In Japan, \"hack\" is commonly a bad word, but surprisingly it has a broader meaning.",
                    meaning = "くしゃみ",
                    note = "上記の意味は誤っているため訂正せよ"
                    )
        word.save()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        add_default(int(sys.argv[1]))
    call()
