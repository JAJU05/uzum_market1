from django.urls import path, include
from rest_framework.routers import DefaultRouter

from uzum.views import ProductModelViewSet, CategoryModelViewSet, ShopModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register('products', ProductModelViewSet, 'products')
router.register('category', CategoryModelViewSet, 'category')
router.register('seller', ShopModelViewSet, 'seller')
router.register('order', OrderModelViewSet, 'order')

urlpatterns = [
    path('', include(router.urls)),
]
