from utils.dw_utils import DWConnectionUtils

class EmpresaRepository:
    """
    Repository para consultar empresas desde el DW.
    Utiliza psycopg2 y credenciales desde variables de entorno/configuración.
    """

    @staticmethod
    def listar_empresas_g1():
        """
        Retorna un listado de empresas del grupo G1 basado en RUTs específicos.
        Consulta la tabla maestro_rut filtrando por los RUTs definidos en el SQL.
        """
        sql = DWConnectionUtils.sql_load('warehouse', 'listar_empresas_g1.sql')
        return DWConnectionUtils.fetch_dicts(sql)

    @staticmethod
    def obtener_empresa_por_rut(rut):
        """
        Obtiene información de una empresa específica por su RUT.
        
        Args:
            rut (str): RUT de la empresa a consultar
            
        Returns:
            dict: Información de la empresa o None si no se encuentra
        """
        sql = "SELECT mr.* FROM public.maestro_rut AS mr WHERE rut = %s"
        result = DWConnectionUtils.fetch_dicts(sql, [rut])
        return result[0] if result else None

    @staticmethod
    def verificar_empresa_g1(rut):
        """
        Verifica si un RUT pertenece al grupo G1 de empresas.
        
        Args:
            rut (str): RUT a verificar
            
        Returns:
            bool: True si pertenece al grupo G1, False en caso contrario
        """
        empresas_g1 = EmpresaRepository.listar_empresas_g1()
        ruts_g1 = [empresa['rut'] for empresa in empresas_g1]
        return rut in ruts_g1
