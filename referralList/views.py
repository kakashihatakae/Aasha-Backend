from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import menteeRowInfo
from .serializer import *

# https://blog.logrocket.com/creating-an-app-with-react-and-django/
# https://www.geeksforgeeks.org/serializer-relations-django-rest-framework/
# https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react


@api_view(['POST', 'GET'])
def studentInfo(request):
    if request.method == 'GET':
        data = menteeRowInfo.objects.all()
        Serialiser = menteeRowInfoSerializer(
            data, many=True)
        return Response(Serialiser.data)

    if request.method == 'POST':
        dataInstance = menteeRowInfoSerializer(data=request.data)
        print(dataInstance)
        if dataInstance.is_valid():
            dataInstance.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(dataInstance.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def RejectStudent(request, pk):
    try:
        rejectedStudent = menteeRowInfo.objects.get(pk=pk)
    except menteeRowInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        rejectedStudent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
