from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    def collection(self, obj):
        return obj.collection.title
    @admin.display(ordering='inventory')
    def inventory_status(self, obj):
        if obj.inventory > 0:
            return 'In Stock'
        return 'Out of Stock'
    # for more info visit https://docs.djangoproject.com/en/4.0/ref/contrib/admin/


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    # for more info visit https://docs.djangoproject.com/en/4.0/ref/contrib/admin/


admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Admin'
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
