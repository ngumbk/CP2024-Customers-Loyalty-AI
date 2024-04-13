from rest_framework import generics, status
from rest_framework.response import Response

from customers_loyalty_app.models import CustomerQuartalFigure

from api.serializers import CustomerQuartalFigureSerializer


class CustomerQuartalFigureAPIView(generics.ListAPIView):
    model = CustomerQuartalFigure
    serializer_class = CustomerQuartalFigureSerializer

    def get_queryset(self):
        queryset = CustomerQuartalFigure.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
