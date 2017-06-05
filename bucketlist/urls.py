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
# from tastypie.api import Api


from bucketlist import api

admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# from bucketlist.api.users import (UserViewSet,
#                                   BucketlistViewSet,
#                                   BucketlistItemViewSet)


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserRegistrationAPI, base_name='user-registration')
# router.register(r'bucketlist', UserListAPI.as_view(), base_name='bucketlist')
# router.register(r'bucketlistitem', UserDetailAPI.as_view(), base_name='bucketlist-items')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bucketlist.api.urls')),
]


urlpatterns += [
    url(r'^bucketlist/api/auth', include('rest_framework.urls',
                                               namespace='rest_framework')),
]

# print ('\n\n')
# print (urlpatterns)
# print ('\n\n')