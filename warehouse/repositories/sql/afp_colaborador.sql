SELECT afp.* FROM flesan_rrhh.xls_afp_colaborador_gf AS afp 
where np = %{np}s
AND status='A'