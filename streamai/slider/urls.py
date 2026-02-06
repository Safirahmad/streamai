# slider/urls.py
from django.urls import path
from .views import SliderListAPIView

urlpatterns = [
    path('sliders/', SliderListAPIView.as_view()),
]
