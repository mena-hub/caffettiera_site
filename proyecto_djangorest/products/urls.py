from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]