from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import LogViewSet


router = DefaultRouter()
router.register(r'logs', LogViewSet)

urlpatterns = [
    path('', include(router.urls))
]