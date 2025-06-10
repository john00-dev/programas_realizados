from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas automáticamente
]
