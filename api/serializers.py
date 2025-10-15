from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    point_id = serializers.IntegerField()
    items = OrderItemSerializer(many=True)
