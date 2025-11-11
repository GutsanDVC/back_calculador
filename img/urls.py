from django.urls import path
from .views import SAPPhotoProxyView

urlpatterns = [
    path('<int:user_id>/', SAPPhotoProxyView.as_view(), name='sap_photo_proxy'),
]
