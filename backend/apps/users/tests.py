from django.test import TestCase

from apps.users.models import User
from django.utils import timezone

# models test
class UserTest(TestCase):

    def create_test_user(self):
        return User.objects.create_user(email='test@gmail.com', password='test@123')


    def test_user_creation(self):
        u = self.create_test_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.name)
