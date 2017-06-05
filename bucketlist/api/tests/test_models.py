from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from bucketlist.api.models import Bucketlist, BucketlistItem


class UserTestCase(TestCase):
    def setUp(self):
        # Create user
        User.objects.create_user(username="tina",
                                 email="tina.murimi@andela.com",
                                 password='tina123456')

        tina = User.objects.get(username="tina")

        # Create bucketlist
        Bucketlist.objects.create(list_name="camping",
                                  description=None,
                                  created_by=tina)

    def test_user_created_successfully(self):
        """Test a user is created successfully"""

        User.objects.create_user(username="Mark",
                                 email="mark@andela.com",
                                 password='mark123456')

        mark = User.objects.get(username="Mark")

        # user = authenticate(username="Mark", password='mark123456')

        self.assertIsNotNone(mark)
        self.assertEqual("Mark", mark.username)

    def test_bucketlist_created_successfully(self):
        """Test a bucketlist is created successfully"""

        tina = User.objects.get(username="tina")
        Bucketlist.objects.create(list_name="Cycling",
                                  description=None,
                                  created_by=tina)

        cycling = Bucketlist.objects.get(list_name="Cycling")

        self.assertEqual(cycling.list_name, "Cycling")
        self.assertIsNotNone(cycling)

    def test_bucketlist_bulk_create(self):
        """
        Tsst you can bulk create bucketlists
        """

        tina = User.objects.get(username="tina")

        Bucketlist.objects.bulk_create([
            Bucketlist(list_name="Learn Tango",
                       description=None,
                       created_by=tina),
            Bucketlist(list_name="Bungee Jumping",
                       description=None,
                       created_by=tina),
        ])

        bucketlists = Bucketlist.objects.values_list('list_name', flat=True)
        self.assertIn("Bungee Jumping", bucketlists)

    def test_bucketlist_item_created_successfully(self):
        """Test a bucketlist item is created successfully"""

        camping = Bucketlist.objects.get(list_name="camping")
        BucketlistItem.objects.create(item_name="Camping in Aberdare",
                                      description=None,
                                      list_id=camping)

        camping_item = BucketlistItem.objects.get(
            item_name="Camping in Aberdare")

        self.assertEqual(camping_item.item_name, "Camping in Aberdare")
        self.assertIsNotNone(camping_item)
