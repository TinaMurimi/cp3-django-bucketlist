from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from bucketlist.api.models import Bucketlist, BucketlistItem
from bucketlist.serializer import (UserSerializer,
                                   UserPostSerializer,
                                   UsernameSerializer,
                                   BucketlistSerializer,
                                   BucketlistItemSerializer)

# ViewSets define the view behavior.


class UserPostViewSet(viewsets.ModelViewSet):
    is_private = True
    queryset = User.objects.all()
    serializer_class = UserPostSerializer
    # permission_classes = (WgerPermission, UpdateOnlyPermission)
    ordering_fields = '__all__'


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     is_private = True
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (WgerPermission, UpdateOnlyPermission)
#     ordering_fields = '__all__'

#     def get_queryset(self):
#         '''
#         Only allow access to appropriate objects
#         '''
#         return User.objects.filter(username=self.request.user)

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


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users
    """

    queryset = User.objects.all()

    def list(self, request, pk=None):
        if not pk:
            self.queryset = get_object_or_404(self.queryset, pk=pk)

        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              permissions.IsAdminUser,
                              IsOwnerOrReadOnly,
                              )
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class BucketlistViewSet(viewsets.ModelViewSet):
    is_private = True
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (WgerPermission, UpdateOnlyPermission)
    ordering_fields = '__all__'

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return Bucketlist.objects.filter(created_by=self.request.user)


class BucketlistItemViewSet(viewsets.ModelViewSet):
    is_private = True
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer
    # permission_classes = (WgerPermission, UpdateOnlyPermission)
    ordering_fields = '__all__'

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return BucketlistItem.objects.filter(list_id__created_by=self.request.user)
