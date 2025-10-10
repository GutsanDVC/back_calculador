from django.urls import path
from .views import RangosColacionMovilizacionView

urlpatterns = [
    path('rangos-colacion-movilizacion/', RangosColacionMovilizacionView.as_view(), name='bd-gestion-rangos-colacion-movilizacion'),
]