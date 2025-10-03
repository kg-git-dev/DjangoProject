from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserListCreate(APIView):
    """
    View to list all users or create a new one.
    * Requires token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        """Retrieves and displays details of all users."""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Creates a new user."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    View to retrieve, update or delete a user instance by email.
    * Requires token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get(self, request, email, format=None):
        """Retrieves and displays details of a specific user based on their email."""
        user = self.get_object(email)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, email, format=None):
        """Update User details."""
        user = self.get_object(email)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email, format=None):
        """To delete a user using its email."""
        user = self.get_object(email)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
