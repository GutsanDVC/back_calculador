import mysql.connector
import os

class BDConnectionUtils:
    """
    Utilidad general para obtener una conexión a la Base de Datos de Gestión (MySQL).
    Utiliza variables de entorno para los parámetros de conexión.
    """
    @staticmethod
    def get_bd_connection():
        """
        Retorna una conexión mysql.connector a la BD de gestión usando variables de entorno.
        """
        
        return mysql.connector.connect(
            database=os.getenv('DB_NAME_MS'),
            user=os.getenv('DB_USER_MS'),
            password=os.getenv('DB_PASWORD_MS'),
            host=os.getenv('DB_HOST_MS'),
            port=os.getenv('DB_PORT_MS', 3306)
        )

    @staticmethod
    def sql_load(modulo: str, archivo: str) -> str:
        """
        Carga el contenido de un archivo SQL ubicado en <modulo>/repositories/sql/<archivo>.
        Args:
            modulo: Nombre del módulo (ej: 'warehouse').
            archivo: Nombre del archivo SQL (ej: 'listar_colaboradores.sql').
        Returns:
            Contenido del archivo SQL como string.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sql_path = os.path.join(base_dir, modulo, 'repositories', 'sql', archivo)
        with open(sql_path, encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def fetch_dicts(sql: str, params=None) -> list:
        """
        Ejecuta una consulta SQL y retorna los resultados como lista de diccionarios.
        Args:
            sql: Consulta SQL a ejecutar.
            params: Parámetros opcionales para la consulta.
        Returns:
            Lista de diccionarios con los resultados.
        """
        results = []
        with BDConnectionUtils.get_bd_connection() as conn:
            #print(sql) # DEBUG
            with conn.cursor(dictionary=True) as cur:  # dictionary=True para obtener resultados como dict
                cur.execute(sql, params or [])
                results = cur.fetchall()
                #print(results) # DEBUG
        return results

    @staticmethod
    def execute_query(sql: str, params=None) -> int:
        """
        Ejecuta una consulta SQL de modificación (INSERT, UPDATE, DELETE) y retorna el número de filas afectadas.
        Args:
            sql: Consulta SQL a ejecutar.
            params: Parámetros opcionales para la consulta.
        Returns:
            Número de filas afectadas.
        """
        with BDConnectionUtils.get_bd_connection() as conn:
            #print(sql) # DEBUG
            with conn.cursor() as cur:
                cur.execute(sql, params or [])
                conn.commit()  # Confirmar los cambios
                return cur.rowcount

    @staticmethod
    def fetch_one_dict(sql: str, params=None) -> dict:
        """
        Ejecuta una consulta SQL y retorna el primer resultado como diccionario.
        Args:
            sql: Consulta SQL a ejecutar.
            params: Parámetros opcionales para la consulta.
        Returns:
            Diccionario con el primer resultado o None si no hay resultados.
        """
        with BDConnectionUtils.get_bd_connection() as conn:
            #print(sql) # DEBUG
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, params or [])
                result = cur.fetchone()
                #print(result) # DEBUG
        return result
