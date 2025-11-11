from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories.colaborador_repository import ColaboradorRepository

class CumpleanosView(APIView):
    def get (self, request, *args, **kwargs):
        try:
            cumpleanos = ColaboradorRepository.obtener_cumpleanos_por_fecha(request.query_params.get('to_date'))
            return Response(cumpleanos, status=status.HTTP_200_OK)
        except Exception as e:
            # Retorna error genérico y mensaje para debug
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CumpleanosMesView(APIView):
    def get (self, request, *args, **kwargs):
        try:
            cumpleanos = ColaboradorRepository.obtener_cumpleanos_mes_por_fecha(request.query_params.get('to_date'))
            return Response(cumpleanos, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)