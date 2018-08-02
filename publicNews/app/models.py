from django.db import models
from .fields import RichTextField
from .fields import RichTextUploadingField
# Create your models here.
class NewsPublic(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    # content = RichTextField(max_length=5000, null=True,blank=True)
    # content = RichTextUploadingField( null=True,blank=True,external_plugin_resources=[('easyimage','/static/ckeditor/plugins/easyimage/','plugin.js')],)
    content = RichTextUploadingField( null=True,blank=True)
    url=models.CharField(max_length=500,blank=True,null=True)
    file = models.FileField(blank=True)
    image = models.ImageField(blank=True,null=True)
