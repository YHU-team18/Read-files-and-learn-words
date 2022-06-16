from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    meaning_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ["-importance"]

class Meaning(models.Model):
    #word_意味のクラス
    meaning = models.TextField()
    word = models.OneToOneField(Word, on_delete=models.CASCADE)

class Pronunce(models.Model):
    #word_発音のクラス
    pronunce = models.BinaryField()
    word = models.OneToOneField(Word, on_delete=models.CASCADE)

class Phonetics(models.Model):
    #word_発音記号のクラス
    Phonetics = models.CharField()
    word = models.OneToOneField(Word, on_delete=models.CASCADE)

class Frequency(models.Model):
    #word_頻度のクラス
    Frequency = models.IntegerField()
    word = models.OneToOneField(Word, on_delete=models.CASCADE)