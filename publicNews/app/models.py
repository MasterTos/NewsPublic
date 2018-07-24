from django.db import models

# Create your models here.
class NewsPublic(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    content = models.TextField(max_length=5000, null=True,blank=True)
    url=models.CharField(max_length=500,blank=True,null=True)
    file = models.FileField(blank=True)
    image = models.ImageField(blank=True,null=True)
