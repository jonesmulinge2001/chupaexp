from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics, response, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from.serializers import RegisterSerializer, UserSerializer

# create classes for registerview, profileview, loginview
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    # create a user
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() # save the user to the database
        return response.Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully. Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)
    
# login
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return response.Response({
                "user": UserSerializer(user).data,
                "message": "Login successful",
            }, status=status.HTTP_200_OK)
        else:
            return response.Response({
                "error": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)   

# profile view
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all() # get the user from the database
    serializer_class = UserSerializer # serialize the user data
    permission_classes = [IsAuthenticated] # only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        user = request.user # get the user from the request
        serializer = self.get_serializer(user) # serialize the user data
        return response.Response(serializer.data, status=status.HTTP_200_OK)