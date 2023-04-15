from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


from uzum.models import Category, Product, Shop, Order, Cart, Favourite


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Favourite)

