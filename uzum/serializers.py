from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from uzum.models import Cart, Product, Category, Favourite, Order, Shop


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        exclude = ()


class OrderCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class CartModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Cart
        exclude = ()


class FavouriteModelSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        exclude = ()
