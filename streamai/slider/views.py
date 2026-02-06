from django.shortcuts import render
# slider/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Slider
from .serializers import SliderSerializer
from rest_framework import status

class SliderListAPIView(APIView):
    
    def get(self, request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)
    def post(self, request):
        """
        POST /sliders/ -> create new slider
        """
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # --------------------- PUT ---------------------
    def put(self, request, pk):
        """
        PUT /sliders/<id>/ -> full update of a slider
        """
        try:
            slider = Slider.objects.get(id=pk)
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # --------------------- PATCH ---------------------
    def patch(self, request, pk):
        """
        PATCH /sliders/<id>/ -> partial update
        """
        try:
            slider = Slider.objects.get(id=pk)
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SliderSerializer(slider, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # --------------------- DELETE ---------------------
    def delete(self, request, pk):
        """
        DELETE /sliders/<id>/ -> delete slider
        """
        try:
            slider = Slider.objects.get(id=pk)
            slider.delete()
            return Response({"message": "Slider deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found"}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
