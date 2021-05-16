from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, PostOwnStatus


class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        context = {"message": "Hello"}
        return Response(context)

    def post(self, request):
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            context = {'message': message}
            return Response(context)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        context = {"method": "put"}
        return Response(context)

    def patch(self, request, pk=None):
        context = {"method": "patch"}
        return Response(context)

    def delete(self, request, pk=None):
        context = {"method": "Delete"}
        return Response(context)


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello Message"""
        viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        context = {"message": "Hello", "viewset": viewset}
        return Response(context)

    def create(self, request):
        """Create a new hello message"""
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            context = {"message": message}
            return Response(context)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handling getting an object by its ID"""
        context = {"Http Method": "GET"}
        return Response(context)

    def update(self, request, pk=None):
        """Handles updating an Object"""
        context = {"Http Method": "PUT"}
        return Response(context)

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        context = {"Http method": "PATCH"}
        return Response(context)

    def destroy(self, request, pk=None):
        """Handles Removing an object"""
        context = {"Http Response": "Delete"}
        return Response(context)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Obtain the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handling creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (PostOwnStatus, IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Set the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)







