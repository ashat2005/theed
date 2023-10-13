from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.yu.urls import router as MailViewSet

router = DefaultRouter()

router.registry.extend(MailViewSet.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.yu.urls')),
]
