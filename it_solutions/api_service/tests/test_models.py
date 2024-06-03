from django.test import TestCase
from api_service.models import Advertisement


class TestAdvertisementModel(TestCase):

    def setUp(self):
        self.advertisement = Advertisement.objects.create(
            title='test_advertisement_title',
            author='test_advertisement_author',
            count_views=1,
            position=1
        )

    def test_str_method(self):
        correct_meaning = self.advertisement.title
        self.assertEqual(str(self.advertisement), correct_meaning)
