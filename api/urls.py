from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register('api/boards', BoardViewSet, 'board')
router.register('api/openings', OpeningViewSet, 'opening')
router.register('api/computers', ComputerViewSet, 'computers')
router.register('api/games', GameViewSet, 'games')

urlpatterns = router.urls
