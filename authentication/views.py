from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        user = serializer.save()

        return Response({
            "message": "User registered successfully.",
            "user": {
                "username": user.username,
                "email": user.email,
                "farm_size": user.farm_size,
                },
        }, status=status.HTTP_201_CREATED)
    
class LoginView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    # Implement login logic here
    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']

        # generate token logic to be added here

        return Response({
            "message": "Login Successful.",
            "user": {
                "username": user.username,
                "email": user.email,
                "farm_size": user.farm_size,
                # "token": token,  # Include token when implemented
            },  
        }, status=status.HTTP_200_OK)