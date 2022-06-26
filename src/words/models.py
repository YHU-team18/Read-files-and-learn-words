from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Meaning(models.Model):
    """
    単語の意味と単語を持ち合わせている.
    事前にsrcの中に保存されている

    Args:
        models (_type_): _description_
    """
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=200)

# Create your models here.
class Word(models.Model):
    """ Wordのclass

    Args:
        models (_type_): _description_
    """
    word = models.CharField(max_length=100)
    importance = models.IntegerField(validators=[MinValueValidator(-10), MaxValueValidator(100)])
    example_sentence = models.TextField(blank=True)
    meaning = models.TextField()
    note = models.TextField(blank=True)

    thesis_id = models.IntegerField(blank=True, null=True) # 本当は自動補完したい
    pronounce_id = models.IntegerField(blank=True, null=True)
    phonetics_id = models.IntegerField(blank=True, null=True)
    
    meaning_id = models.ForeignKey(Meaning, null=True, on_delete=models.SET_NULL, related_name='id')
    default_meaning = models.ForeignKey(Meaning, null=True, on_delete=models.SET_NULL, related_name='meaning')

    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ["-importance"]
