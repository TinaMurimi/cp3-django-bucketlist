# Register the models with the admin app

from django.contrib import admin

from django.contrib import admin
from bucketlist.api.models import Bucketlist, BucketlistItem

# admin.site.register(User)
admin.site.register(Bucketlist)
admin.site.register(BucketlistItem)
