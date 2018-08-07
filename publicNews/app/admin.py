from django.contrib import admin
from .models import NewsPublic
# Register your models here.
class publicAdmin(admin.ModelAdmin):
	list_display=[f.name for f in NewsPublic._meta.fields]
	list_editable = ['image','title','description',]

admin.site.register(NewsPublic,publicAdmin)
