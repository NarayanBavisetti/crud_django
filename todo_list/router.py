from todo.viewsets import StatusViewset, TodoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo',TodoViewset)
router.register('status',StatusViewset)