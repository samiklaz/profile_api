from rest_framework import serializers
from .models import *


class HelloSerializer(serializers.Serializer):
    """ Seralizes a name field for testing out APIView """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile object"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Create and return a new user"""
        email = validated_data['email']
        name = validated_data['name']
        password = validated_data['password']
        user = UserProfile(email=email, name=name)
        user.set_password(password)
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }