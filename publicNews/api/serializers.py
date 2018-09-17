from rest_framework import serializers
from app.models import Newspublic

class NewsSerialzer(serializers.ModelSerializer):
    # news = serializers.SlugRelatedField(read_only='True',slug_field = 'title')
    class Meta:
        model = Newspublic
        fields = ['id','title','date', 'description','content','image' ]