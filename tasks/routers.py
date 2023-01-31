from rest_framework import routers

from .viewsets import MissingTaskViewSet

router = routers.DefaultRouter()
router.register(r"v1/tasks", MissingTaskViewSet)