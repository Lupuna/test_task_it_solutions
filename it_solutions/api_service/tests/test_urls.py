from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api_service.views import AdvertisementView


class TsetUrls(SimpleTestCase):

    def test_detail_advertisement_url_is_resolve(self):
        url = reverse('advertisement:detail-advertisement', args=[1])
        self.assertEqual(resolve(url).func.view_class, AdvertisementView)

