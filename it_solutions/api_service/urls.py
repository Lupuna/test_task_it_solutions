from django.urls import path
from api_service.views import AdvertisementView


app_name = 'advertisement'


urlpatterns = [
    path('<int:id>', AdvertisementView.as_view(), name='detail-advertisement'),
]
