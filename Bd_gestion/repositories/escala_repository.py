from utils.bd_utils import BDConnectionUtils

class EscalaRepository:
    """
    Repository para manejar consultas relacionadas con la tabla escala de la BD de gestión.
    """
    
    @staticmethod
    def obtener_rangos_colacion_movilizacion():
        """
        Obtiene los rangos de colación y movilización agrupados con sus valores mínimo y máximo.
        
        Returns:
            list: Lista de diccionarios con colacion, movilizacion, minimo y maximo
        """
        sql = BDConnectionUtils.sql_load('Bd_gestion', 'rangos_colacion_movilizacion.sql')
        return BDConnectionUtils.fetch_dicts(sql)
