from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import KlassViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'klass', KlassViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Sizning API loyihangiz",
        default_version='v1',
        description="API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aloqa@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
