from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserLoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        return Response({})

    
class UserSignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


