"""bucketlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from bucketlist.api import views
from bucketlist.api.users import (UserRegistrationAPI,
                                  UserListAPI,
                                  UserDetailAPI)

from bucketlist.api.views import (UserViewSet,
                                  UserPostViewSet,
                                  BucketlistViewSet,
                                  BucketlistItemViewSet)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'register', UserPostViewSet, base_name='user-registration')
router.register(r'users', UserViewSet, base_name='user-details')
router.register(r'bucketlist', BucketlistViewSet, base_name='bucketlist')
router.register(r'bucketlistitem', BucketlistItemViewSet,
                base_name='bucketlist-items')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'bucketlist/api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='all_rest_framework')),
]


urlpatterns += [
    url(r'^bucketlist/api/register$',
        UserRegistrationAPI.as_view(),
        name="User-registration"),
    url(r'^bucketlist/api/users$',
        UserListAPI.as_view(),
        name="User-list"),
    url(r'^bucketlist/api/users/(?P<pk>[0-9]+)/$',
        UserDetailAPI.as_view(),
        name="User-details"),
]

# urlpatterns += [
#     url(r'^bucketlist/api/auth/login', include('rest_framework.urls',
#                                                 namespace='rest_framework')),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
