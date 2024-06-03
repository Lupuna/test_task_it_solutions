from api_service.models import Advertisement
from api_service.serializes import AdvertisementGetSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from django.conf import settings


class AdvertisementView(RetrieveAPIView):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementGetSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        advertisement_cache = cache.get(settings.ADVERTISEMENT_CACHE)
        if advertisement_cache is None:
            response = super().get(request, *args, **kwargs)
            cache.set(settings.ADVERTISEMENT_CACHE, response, 60*60)
        return advertisement_cache



