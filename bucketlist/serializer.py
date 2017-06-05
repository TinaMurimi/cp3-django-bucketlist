# Serializers define the API representation.

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from bucketlist.api.models import Bucketlist, BucketlistItem


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserPostSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        model = User
        fields = (
            # "url",
            'id',
            'username',
            # 'full_name',
            'email',
            'last_login',
        )

    # full_name = serializers.SerializerMethodField('get_full_name')


class UsernameSerializer(serializers.Serializer):
    '''
    Serializer to extract the username
    '''
    username = serializers.CharField()


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Bucketlist serializer
    """

    class Meta:
        model = Bucketlist
        fields = (
            'list_id',
            'list_name',
            'description',
            'is_completed',
            'created_on',
            'date_modified',
            'created_by',
        )


class BucketlistItemSerializer(serializers.ModelSerializer):
    """
    Bucketlist Item serializer
    """

    class Meta:
        model = BucketlistItem
        fields = (
            'item_id',
            'list_id',
            'item_name',
            'description',
            'is_completed',
            'created_on',
            'date_modified',
        )
