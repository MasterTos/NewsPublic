from django.contrib import admin
from .models import Newspublic
# Register your models here.
class publicAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Newspublic._meta.fields]
	list_editable = ['image','title','description',]

admin.site.register(Newspublic,publicAdmin)

