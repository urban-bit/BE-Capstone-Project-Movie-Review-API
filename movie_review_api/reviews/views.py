# reviews/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing review instances.
    Allows users to create, update, and delete their own reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # Add filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie_title', 'rating']

    def perform_create(self, serializer):
        """
        Set the user to the current authenticated user when creating a new review.
        """
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides read-only actions for User model.
    Allows users to list all users or retrieve details of a specific user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
# 