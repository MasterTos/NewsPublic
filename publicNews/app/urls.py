from django.urls import path
from . import views

urlpatterns = [
    path('' , views.news_public , name="newpublic"),
    path('news/<int:id>/' , views.detail_public, name="detialpublic"),
    path('upload/',views.public_upload, name="upload"),
    path('edit/<int:id>/' ,views.pub_update, name="edit"),
    path('delete/<int:id>/' ,views.public_delete, name="delete"),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)