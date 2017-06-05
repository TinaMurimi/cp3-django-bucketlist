from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from rest_framework import generics, mixins, permissions, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from bucketlist.api.models import Bucketlist, BucketlistItem
from bucketlist.api.permissions import IsOwnerOrReadOnly

from bucketlist.serializer import (UserPostSerializer,
                                   UserSerializer,
                                   UsernameSerializer,
                                   BucketlistSerializer,
                                   BucketlistItemSerializer)


class UserRegistrationAPI(generics.CreateAPIView):
    """
    Create a new user
    """

    is_private = True
    queryset = User.objects.all()
    serializer_class = UserPostSerializer
    ordering_fields = '__all__'

    def post(self, request, format=None):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Bits of common behaviour are implemented in REST framework's mixin classes
# The base class provides the core functionality, and the mixin classes provide
# the .list() and .create() actions

# class UserListAPI(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     """
#     List all users
#     """

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class UserListAPI(generics.ListAPIView):
    """
    List all users
    """

    is_private = True
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,
                          IsOwnerOrReadOnly,
                          )
    ordering_fields = '__all__'

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserListAPI(generics.ListAPIView):
#     """
#     List all users
#     """

#     is_private = True
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,
#                           )
#     ordering_fields = '__all__'

#     # @login_required
#     def get(self, request, format=None):
#         user = User.objects.all()
#         serializer = UserSerializer(user, many=True)

#         # user = User.objects.get(username=self.request.user)
#         # serializer = UserSerializer(user)

#         return Response(serializer.data)

#     def get_queryset(self):
#         """
#         Only allow access to appropriate objects
#         """
#         # pass
#         return User.objects.filter(username=self.request.user)
#         # return User.objects.all()

#     def get_owner_objects(self):
#         '''
#         Return objects to check for ownership permission
#         '''
#         return [(User, 'user')]

#     @detail_route()
#     def username(self, request, pk):
#         '''
#         Return the username
#         '''

#         user = self.get_object().user
#         return Response(UsernameSerializer(user).data)


# Bits of common behaviour are implemented in REST framework's mixin classes
# class UserDetailAPI(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """
#     Retrieve, update or delete a user instance
#     """

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserDetailAPI(APIView):
#     """
#     Retrieve, update or delete a user instance
#     """

#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')
