from rest_framework import viewsets,mixins,filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NewsSerialzer
from app.models import Newspublic
class NewsPublicViewset(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet
                    ):
    queryset            = Newspublic.objects.all()
    serializer_class    = NewsSerialzer
    filter_backends     = (filters.SearchFilter,)
    # filter_fields       = ('name','last_name')
    search_fields       = ('title','date', 'description','content')