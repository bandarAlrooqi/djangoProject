from django.contrib import admin
from . import models


# important note to remove the field validation just add blank=True to the field
# for example: name = models.CharField(max_length=100, blank=True)
# this will remove the validation for the field
# we can also import validators from django.core.validators import MinLengthValidator
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title', 'description']

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
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_per_page = 10
    # for more info visit https://docs.djangoproject.com/en/4.0/ref/contrib/admin/


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = ['total_price']
    autocomplete_fields = ['product']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'placed_at', 'payment_status']
    list_select_related = ['customer']
    list_per_page = 10
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]


admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Admin'
