from django.db import models
from expense_management.accounts.models import User

TAG_COLOR_CHOICES = (
    ('B', 'Blue'),
    ('R', 'Red'),
    ('G', 'Green'),
    ('Y', 'Yellow'),
    ('O', 'Orange'),
    ('P', 'Purple'),
)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=1, choices = TAG_COLOR_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Expense(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
    expense_date = models.DateTimeField()
    description = models.TextField(blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name