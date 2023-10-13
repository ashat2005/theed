from rest_framework.routers import DefaultRouter
from .views import MailViewSet

router = DefaultRouter()

router.register(r'mail', MailViewSet, basename='mail')

urlpatterns = router.urls