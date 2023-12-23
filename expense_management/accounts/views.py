# accounts/views.py
import logging
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class CustomLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        print('Email ', request.data)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user and user.check_password(password):
            # Authentication successful
            login(request, user)
            print(user)
            logging.info(f"User {email} logged in successfully.")
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            logging.warning(f"Failed login attempt for user {email}.")
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
