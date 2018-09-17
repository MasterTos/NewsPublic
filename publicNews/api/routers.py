from rest_framework import routers
from .viewsets import NewsPublicViewset
router = routers.DefaultRouter()
router.register(r'newspublic',NewsPublicViewset) 