from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

# from shop.filters import ProductFilter
from uzum.models import Category, Product, Shop, Cart, Favourite, Order
from uzum.permissions import IsOwner
from uzum.serializers import CategoryModelSerializer, ProductModelSerializer, CartModelSerializer, \
    ShopModelSerializer, FavouriteModelSerializer, OrderCreateModelSerializer
# from user.permissions import IsOwner


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_class = {'real_price': ['gte', 'lte'],}
    search_fields = ['name']
    ordering_fields = ['price']
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class WishlistModelViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateModelSerializer
    permission_classes = (IsAuthenticated, IsOwner,)
