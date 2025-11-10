SELECT 
    CAST(%(fecha)s AS date) AS fecha,
    CAST(c.fecha_nacimiento_date AS date) AS fecha_nacimiento_date,
    c.user_id::INT,
    c.first_name,
    c.last_name,
    c.empl_status,
    c.centro_costo,
    c.nombre_centro_costo,
    c.external_cod_cargo
FROM 
    flesan_rrhh.sap_maestro_colaborador AS c
WHERE 
    c.empl_status = '41111'
    AND TO_CHAR(CAST(c.fecha_nacimiento_date AS date), 'MM-DD') = TO_CHAR(CAST(%(fecha)s AS date), 'MM-DD');