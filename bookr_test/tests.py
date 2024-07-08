from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from .models import PublisherTest
from .views import greeting_view_user

# Create your tests here.


class TestPublisherModel(TestCase):
    """Test the publisher model"""

    def setUp(self):
        self.p = PublisherTest(name='Packt',
                               website='www.packt.com',
                               email='contact@packt.com')

        self.client = Client()

    def test_create_publisher(self):
        self.assertIsInstance(self.p, PublisherTest)

    def test_str_representation(self):
        self.assertEqual(str(self.p), "Packt")

    def test_greeting_view(self):
        response = self.client.get("/test/greeting")
        self.assertEqual(response.status_code, 200)


class TestLoggedInGreetingView(TestCase):
    """Test the greeting view for the authenticated users"""

    def setUp(self):
        test_user = User.objects.create_user(username='testuser',
                                             password='test@#628password')
        test_user.save()
        self.client = Client()

    def test_user_greeting_not_authenticated(self):
        response = self.client.get('/test/greet_user')
        self.assertEqual(response.status_code, 302)

    def test_user_authenticated(self):
        login = self.client.login(username='testuser',
                                  password='test@#628password')
        response = self.client.get('/test/greet_user')
        self.assertEqual(response.status_code, 200)


class TestLoggedInGreetingView_with_RequestFactory(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_greeting_not_authenticated(self):
        request = self.factory.get('/test/greet_user')
        request.user = AnonymousUser()
        response = greeting_view_user(request)
        self.assertEqual(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/test/greet_user')
        request.user = self.test_user
        response = greeting_view_user(request)
        self.assertEqual(response.status_code, 200)
