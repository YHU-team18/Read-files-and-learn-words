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
    example_sentence = models.TextField()
    meaning = models.TextField()
    note = models.TextField()

    thesis_id = models.AutoField()
    pronounce_id = models.AutoField()
    phonetics_id = models.AutoField()
    meaning_id = models.AutoField()

    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ["-importance"]

