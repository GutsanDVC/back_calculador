SELECT 
    e.colacion, 
    e.movilizacion, 
    MIN(e.liquido) AS minimo, 
    MAX(e.liquido) AS maximo
FROM gestionf_sip_obra.escala AS e
GROUP BY e.colacion, e.movilizacion 
ORDER BY e.colacion
