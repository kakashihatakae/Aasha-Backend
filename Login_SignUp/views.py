from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import status
from .serializer import *
from .models import *
from django.contrib.auth import authenticate
# Create your views here.


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        print('-------------')
        dataInstance = LoginInfoSerializer(data=request.data)
        print([k for k in dataInstance])
        if dataInstance.is_valid():
            print('((((((((((((((((((((')
            print(dataInstance)
            print(')))))))))))))))))))))')
            if authenticate(dataInstance) is not None:
                print('loggedin')
            else:
                print('invalid')
        return Response(status=status.HTTP_201_CREATED)
