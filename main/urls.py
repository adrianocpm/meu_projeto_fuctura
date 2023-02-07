from rest_framework.routers import DefaultRouter
from .views import ConcessionariaViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'concessionaria', ConcessionariaViewSet)

urlpatterns = router.urls

