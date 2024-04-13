from django.urls import path

from .views import CustomerQuartalFigureAPIView

urlpatterns = [
    path('CustomerQuartalFigure', CustomerQuartalFigureAPIView.as_view(), name='CustomerQuartalFigure'),
]
