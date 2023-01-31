from django.db import models

class Question(models.Model):
    rid = models.AutoField(primary_key=True)
    
