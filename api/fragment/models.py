from django.db import models
from text.models import Text

CHOICES = (
    ('1', 'To translate'),
    ('2', 'Translating'),
    ('3', 'To review'),
    ('4', 'Reviewing'),
    ('5', 'To finish'),
    ('6', 'Finished')
)

class Fragment(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    content = models.TextField()
    value = models.FloatField(default=0)
    state = models.CharField(max_length=12, choices=CHOICES, default='1')
    total_reviews = models.IntegerField(default=0)
    translator = models.IntegerField(blank=True, null=True) # id_translator