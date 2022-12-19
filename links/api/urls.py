from rest_framework import routers

from links.api.viewsets import LinkViewSet


router = routers.SimpleRouter()
router.register(r'links', LinkViewSet)

urlpatterns = router.urls
