import requests
from django.http import HttpResponse
from django.views import View
import os
import logging

logger = logging.getLogger(__name__)

class SAPPhotoProxyView(View):
    def get(self, request, user_id):
        try:
            sap_url = f"https://api19.sapsf.com/odata/v2/Photo(userId='{user_id}',photoType=1)/$value"
        
            sap_user = os.getenv('SAP_USER')
            sap_password = os.getenv('SAP_PASSWORD')
            response = requests.get(sap_url, auth=(sap_user, sap_password), stream=True)

            if response.status_code == 200 and response.content:
                content_type = response.headers.get('Content-Type', 'image/jpeg')

                http_response = HttpResponse(response.content, content_type=content_type)
                # Cache por 1 día (24 horas)
                http_response['Cache-Control'] = 'max-age=86400, public'

                return http_response
            else:
                logger.warning(f"SAP no devolvió imagen válida para user_id={user_id}")
                return HttpResponse("", content_type="text/plain", status=200)

        except Exception as e:
            logger.error(f"Error al obtener foto de SAP para {user_id}: {str(e)}")
            return HttpResponse("", content_type="text/plain", status=200)
