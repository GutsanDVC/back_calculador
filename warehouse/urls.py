from django.urls import path
from .views import SapMaestroColaboradorListView, ExternalCode162ListView, ColaboradorPorCorreoView, CompensacionPorNpView,AfpPorNpView
from .views_centro_costo import CentroCostoListView
from .causal_termino_view import CausalTerminoListView
from .views_uf import UfByDateView, UtmUfByDateView
from .views_aniversario import AnniversaryView, AnniversaryMesView
from .views_cumple import CumpleanosView, CumpleanosMesView

urlpatterns = [
    path('colaboradores/', SapMaestroColaboradorListView.as_view(), name='warehouse-colaboradores-list'),
    path('colaborador-por-correo/', ColaboradorPorCorreoView.as_view(), name='warehouse-colaborador-por-correo'),
    path('compensacion-por-np/', CompensacionPorNpView.as_view(), name='warehouse-compensacion-por-np'),
    path('afp-por-np/', AfpPorNpView.as_view(), name='warehouse-afp-por-np'),
    path('centros-costo/', CentroCostoListView.as_view(), name='warehouse-centros-costo-list'),
    path('causales-termino/', CausalTerminoListView.as_view(), name='warehouse-causales-termino-list'),
    path('external-code-162/', ExternalCode162ListView.as_view(), name='warehouse-external-code-162-list'),
    # Endpoint para consultar el valor de la UF según una fecha dada
    path('uf/', UfByDateView.as_view(), name='warehouse-uf-by-date'),
    path('utm-uf/', UtmUfByDateView.as_view(), name='warehouse-utm-uf-by-date'),
    path('cumpleanos/', CumpleanosView.as_view(), name='warehouse-cumpleanos'),
    path('cumpleanos-mes/', CumpleanosMesView.as_view(), name='warehouse-cumpleanos-mes'),
    path('aniversario/', AnniversaryView.as_view(), name='warehouse-aniversario'),
    path('aniversario-mes/', AnniversaryMesView.as_view(), name='warehouse-aniversario-mes'),
]
