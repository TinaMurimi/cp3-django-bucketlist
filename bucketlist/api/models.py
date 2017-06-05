# These are the models for the application

from django.db import models
from django.contrib.auth.hashers import (
    is_password_usable,
    check_password,
    make_password)
from django.contrib.auth.models import User


from datetime import datetime
# datetime.now().isoformat(sep=' ', timespec='minutes')


# class User(models.Model):

#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20, unique=True, null=False)
#     email = models.EmailField(max_length=50, unique=True, null=False)
#     password = models.CharField(max_length=255, null=False)
#     authenticated = models.BooleanField(null=False, default=False)
#     active = models.BooleanField(null=False, default=True)
#     admin = models.BooleanField(null=False, default=False)
#     created_on = models.DateTimeField()
#     last_login = models.DateTimeField()

#     class Meta:
#         db_table = 'User'
#         ordering = ["username"]
#         verbose_name_plural = "users"

#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = make_password(password)
#         self.authenticated = False
#         self.active = False
#         self.created_on = datetime.now().isoformat(
#             sep=' ',
#             timespec='minutes')

#     def __repr__(self):
#         return '<User %r>' % (self.username)

#     def get_id(self):
#         """Return username to satisfy login requirements"""
#         return self.username

#     def is_authenticated(self):
#         """Return True if the user is authenticated"""
#         return self.authenticated

#     def is_active(self):
#         """Return if user has activated their account"""
#         return self.active

#     def is_anonymous(self):
#         """False, as anonymous users aren't supported"""
#         return False

#     def last_login_date(self):
#         """Set date of last login"""
#         return datetime.now().isoformat(sep=' ', timespec='minutes')

#     def verify_password(self, pwd):
#         """Check if passwords match"""
#         return check_password(self.password, pwd)

#     def password_is_hashed(self, pwd):
#         """Check if password is hashed"""
#         return is_password_usable(self.password)


class Bucketlist(models.Model):

    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=20, unique=True, null=False)
    description = models.TextField(max_length=100, null=True)
    is_completed = models.BooleanField(null=False, default=False)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Bucketlist'
        verbose_name_plural = "bucketlists"

    def __repr__(self):
        """Return Bucketlist name"""
        return '<Bucketlist %r>' % (self.list_name)


class BucketlistItem(models.Model):

    item_id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Bucketlist, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20, unique=True, null=False)
    description = models.TextField(max_length=100, null=True)
    is_completed = models.BooleanField(null=False, default=False)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'BucketlistItem'
        verbose_name_plural = "bucketlistitems"

    def __repr__(self):
        """Return Bucketlist item name"""
        return '<Bucketlist %r>' % (self.item_name)
