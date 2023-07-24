from django.contrib import admin
from django.urls import path, include
from trips.views import DepoimentosViewSet, DepoimentosHomeViewSet, DestinosViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosHomeViewSet, basename='Depoimento-random-list')
router.register('destinos', DestinosViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)