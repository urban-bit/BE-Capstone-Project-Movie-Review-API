from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'content', 'rating', 'user', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'reviews']
