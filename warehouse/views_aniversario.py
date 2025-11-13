from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories.colaborador_repository import ColaboradorRepository
CC_EXCLUDE = ['DMOPR11122PU',
'DMOPR11122GG',
'DMFOP110125G',
'DMFOP110125U',
'DMOPR11116GG',
'DMOPR11116PU',
'DMOPR11116NS',
'DMOPR11117PV',
'DMOPR11123GG',
'DMOPR11123PU',
'DMOPR11124NS',
'DMOPR11124PU',
'DMOPR11124GG',
'DMOPR11124NS',
'DMA049']
class AnniversaryView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            aniversario = ColaboradorRepository.obtener_aniversario_por_fecha(request.query_params.get('to_date'))
            response = [col for col in aniversario if col['centro_costo'] not in CC_EXCLUDE]               
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            # Retorna error genérico y mensaje para debug
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnniversaryMesView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            aniversario = ColaboradorRepository.obtener_aniversario_mes_por_fecha(request.query_params.get('to_date'))
            response = [col for col in aniversario if col['centro_costo'] not in CC_EXCLUDE]               
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            # Retorna error genérico y mensaje para debug
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
