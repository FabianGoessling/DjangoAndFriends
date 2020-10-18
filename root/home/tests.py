from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileTest(TestCase):
    def test_user_model_has_profile(self):
        user = User(email="user@mail.com",
                    username="user",
                    password="abc")
        user.save()

        self.assertTrue(hasattr(user, "profile"))
