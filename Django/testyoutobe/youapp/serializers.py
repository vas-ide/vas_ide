from rest_framework.serializers import ModelSerializer
from youapp.models import SalesOrder

class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder
        field = ["amount", "description"]