from django.contrib import admin
from django.urls import path, include
from trips.views import DepoimentosViewSet, DepoimentosHomeViewSet, DestinosViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="JornadAPI",
      default_version='v1',
      description="Api de destinos e depoimentos de lugares para viajar",
      terms_of_service="#",
      contact=openapi.Contact(email="email@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosHomeViewSet, basename='Depoimento-random-list')
router.register('destinos', DestinosViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)