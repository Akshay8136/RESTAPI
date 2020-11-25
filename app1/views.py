from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializer import employeeSerializer

# Create your views here.

def start(request):
    return render(request, 'Dataentry.html')

class employeelist(APIView):

    def get(self, request):
        employee1 = employee.objects.all()
        serializer = employeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = employeeSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_404_BAD_REQUEST)

