from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories.escala_repository import EscalaRepository
import logging

logger = logging.getLogger(__name__)

class RangosColacionMovilizacionView(APIView):
    """
    Vista para obtener los rangos de colación y movilización con sus valores mínimo y máximo.
    """
    
    def get(self, request):
        """
        Obtiene los rangos de colación y movilización agrupados.
        
        Returns:
            Response: Lista de rangos con colacion, movilizacion, minimo y maximo
        """
        try:
            rangos = EscalaRepository.obtener_rangos_colacion_movilizacion()
            
            return Response({
                'success': True,
                'data': rangos,
                'message': 'Rangos de colación y movilización obtenidos exitosamente'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error al obtener rangos de colación y movilización: {str(e)}")
            return Response({
                'success': False,
                'data': [],
                'message': f'Error al obtener los rangos: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
