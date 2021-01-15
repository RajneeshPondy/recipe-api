
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """
        Creating a new user with an email is successful
        """
        email = 'rajneesh@gmail.com'
        password = "python@123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Creating a new user with an email is normalized"""

        email = 'rajneesh@RENEWBUY.COM'
        password = "python@123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        "Test creatig user with no email raise value error"

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "python123")

    def test_create_new_super_user(self):
        """Create a new super user """
        user = get_user_model().objects.create_superuser(
            'rajneesh',
            'python@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
