from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, LoginSerializer, DeleteUserSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.decorators import api_view

# Create your views here.

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # self.perform_create(serializer)
        user = serializer.save()

        return Response({
            "message": "User registered successfully.",
            "user": {
                "username": user.username,
                "email": user.email,
                "farm_size": user.farm_size,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "state": user.state,
                },
        }, status=status.HTTP_201_CREATED)

class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    # Implement login logic here
    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']

        # generate token logic to be added here
        tokens = user.tokens() 

        return Response({
            "message": "Login Successful.",
            "user": {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "state": user.state,
                "email": user.email,
                "farm_size": user.farm_size,
                },  
            "refresh": tokens["refresh_token"],
            "access": tokens["access_token"],
        }, status=status.HTTP_200_OK)
    
class DeleteUserView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DeleteUserSerializer

    def delete(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']

        serializers.delete_user()

        return Response({
            "message": "User deleted successfully.",
        }, status=status.HTTP_200_OK)