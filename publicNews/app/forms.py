from django import forms
from .models import NewsPublic
from django.utils.translation import gettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class PublicForm(forms.ModelForm):
    class Meta:
        model = NewsPublic
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        labels  = {
            "title" : _("ชื่อเรื่อง"),
            "date" : _("วันที่"),
            "content" : _("รายละเอียด"),
            "file" : _("เอกสารแนบ"),
            "image" : _("รูปภาพ"),
        }
