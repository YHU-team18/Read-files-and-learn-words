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
    phonetic = models.CharField(blank=True, null=True, max_length=100, default='---')
    meaning_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ["-importance"]
        constraints = [
            models.UniqueConstraint(
                fields=["word"],
                name="unique_word"
            ),
        ]
