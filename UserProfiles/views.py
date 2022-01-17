from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import UserProfiles
from .sirealizers import UserProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['POST', 'GET'])
def UserProfilesGetPost(request):
    if request.method == 'POST':
        dataInstance = UserProfileSerializer(data=request.data)
        print(dataInstance)
        print([k for k in request.FILES])
        if dataInstance.is_valid():
            dataInstance.save()
            return Response(status=status.HTTP_200_OK)
        print('---------------')
        print(dataInstance.is_valid())
        return Response(dataInstance.errors, status=status.HTTP_400_BAD_REQUEST)


class kaka(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        dataInstance = UserProfileSerializer(data=request.data)
        print(request.data)
        if dataInstance.is_valid():
            dataInstance.save()
            return Response(status=status.HTTP_200_OK)
        print('---------------_+')
        print(dataInstance.is_valid())
        return Response(dataInstance.errors, status=status.HTTP_400_BAD_REQUEST)
