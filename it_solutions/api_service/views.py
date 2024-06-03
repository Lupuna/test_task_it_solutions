from api_service.models import Advertisement
from api_service.serializes import AdvertisementGetSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class AdvertisementView(RetrieveAPIView):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementGetSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated, )
