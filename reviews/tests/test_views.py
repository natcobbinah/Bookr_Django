from django.test import TestCase, RequestFactory
from reviews.views import index


class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_views(self):
        request = self.factory.get('/index')
        request.session = {}
        response = index(request)
        self.assertEqual(response.status_code, 200)
