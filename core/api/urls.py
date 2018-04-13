from django.urls import include, path
from rest_framework import routers

from core.api.viewsets import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = router.urls
