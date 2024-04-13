from rest_framework import serializers

from customers_loyalty_app.models import CustomerQuartalFigure


class CustomerQuartalFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuartalFigure
        fields = '__all__'
