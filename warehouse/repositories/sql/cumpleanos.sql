with colaboradores as (
SELECT 
    CAST(%(fecha)s AS date) AS fecha,
    CAST(c.fecha_nacimiento_date AS date) AS fecha_nacimiento_date,
    c.user_id::INT,
    c.first_name,
    c.last_name,
    c.empl_status,
    c.centro_costo,
    c.nombre_centro_costo,
    c.genero,
    c.external_cod_cargo,
    cargos.nombre_cargo,
    concat('https://api19.sapsf.com/odata/v2/Photo(userId=',c.user_id, ',photoType=1)/$value') AS img
FROM 
    flesan_rrhh.sap_maestro_colaborador AS c
left join 
flesan_rrhh.sap_maestro_cargos cargos
on
c.external_cod_cargo =cargos.external_code
WHERE 
    c.empl_status = '41111'
    AND TO_CHAR(CAST(c.fecha_nacimiento_date AS date), 'MM-DD') = TO_CHAR(CAST(%(fecha)s AS date), 'MM-DD')
order by TO_CHAR(CAST(c.fecha_nacimiento_date AS date), 'DD')
),
centros_costos as(
SELECT 
	distinct centro_costo
	,empresa
FROM flesan_rrhh.sap_maestro_colaborador AS smc
WHERE 
    empl_status='41111'
order by empresa,centro_costo
),
empresas as (
SELECT mr.* FROM public.maestro_rut AS mr
where rut in (
'76418768-7',
'76780803-8',
'76230125-3',
'76879359-K',
'76948230-K',
'77287778-1',
'77902252-8',
'76675510-0',
'76259020-4',
'76259040-9',
'76474409-8',
'76543353-3',
'76710873-7',
'78086195-9',
'77092703-K'
)),
centros_g1 as(
select centros_costos.centro_costo from centros_costos join
empresas
on centros_costos.empresa=empresas.id_sap
)
select*from colaboradores
join centros_g1
on colaboradores.centro_costo = centros_g1.centro_costo