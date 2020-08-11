from django.urls import path, include

from health_service.views import api_root, HealthInfoViewSet

DEFAULT_METHOD = {"get": "get", "post": "post"}

urlpatterns = [
    path('hec', api_root),
    path('hec/health/', HealthInfoViewSet.as_view(DEFAULT_METHOD), name='health-info'),
]

