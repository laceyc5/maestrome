from django.db import models

# Create your models here.
class Advertisement(models.Model):
    ad_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
