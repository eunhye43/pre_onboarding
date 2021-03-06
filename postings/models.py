from django.db import models
from users.models import User

class Posting(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    title      = models.CharField(max_length=50)
    content    = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'postings'
