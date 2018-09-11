from django import forms
from .models import Newspublic
from django.utils.translation import gettext_lazy as _
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class PublicForm(forms.ModelForm):
    class Meta:
        model = Newspublic
        fields = '__all__'
        widgets = {
            'date': DateInput( ),
        }
        labels  = {
            "title" : _("ชื่อเรื่อง"),
            "date" : _("วันที่"),
            "description" : _("รายละเอียด"),
            "content" : _("เนื้อหาข่าว"),
            "image" : _("รูปภาพ"),
        }
