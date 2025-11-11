from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories.colaborador_repository import ColaboradorRepository

class AnniversaryView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            aniversario = ColaboradorRepository.obtener_aniversario_por_fecha(request.query_params.get('to_date'))
            return Response(aniversario, status=status.HTTP_200_OK)
        except Exception as e:
            # Retorna error genérico y mensaje para debug
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnniversaryMesView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            aniversario = ColaboradorRepository.obtener_aniversario_mes_por_fecha(request.query_params.get('to_date'))
            return Response(aniversario, status=status.HTTP_200_OK)
        except Exception as e:
            # Retorna error genérico y mensaje para debug
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
