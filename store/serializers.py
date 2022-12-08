from decimal import Decimal
from rest_framework import serializers
from store.models import Product


class ColliectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='tax_calculator')
    collection = ColliectionSerializer()

    def tax_calculator(self, product: Product):
        return product.unit_price * Decimal(1.1)
