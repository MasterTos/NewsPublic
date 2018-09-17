from django.db import models
from .fields import RichTextField
from .fields import RichTextUploadingField
import datetime
# Create your models here.
class Newspublic(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(default=datetime.date.today,blank=False)
    image = models.ImageField(blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    content = RichTextUploadingField( null=True,blank=True)
    
    def __str__(self):
        return self.title
