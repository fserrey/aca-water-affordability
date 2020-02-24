USE aca_epf;
SELECT * FROM home_ine;

SELECT COUNT(distinct id_d) FROM home_ine
where impexac <> ''
and IMPEXAC is not null;

SELECT COUNT(distinct id_d) FROM home_ine
where impexacpsp != ''
and IMPEXACPSP is not null;

###########AÑADIENDO NUEVA COLUMNA DE TABLA MADRE#################
ALTER TABLE home_ine ADD COLUMN IMPEXAC INTEGER UNSIGNED DEFAULT 0;
UPDATE home_ine t1 
INNER JOIN hogar_ine t2 ON t1.id_d = t2.id_d 
SET t1.IMPEXAC = t2.IMPEXAC;
############################


SELECT gasto.ANOENC,gasto.CODIGO, SUM(IF(((gasto.GASTO/12)/hogar.IMPEXAC)*100 > 5, 1,0)) FLAG
FROM aca_epf.gastos_ine gasto
LEFT JOIN (SELECT home_ine.id_d ,home_ine.ANOENC, home_ine.IMPEXAC 
			FROM home_ine ) hogar ON gasto.id_d = hogar.id_d
WHERE CODIGO between '04511' and '04551'
group by 1,2;

SELECT gasto.ANOENC,gasto.CODIGO, SUM(IF(((gasto.GASTO/12)/hogar.IMPEXACPSP)*100 > 5, 1,0)) FLAG
FROM aca_epf.gastos_ine gasto
LEFT JOIN (SELECT home_ine.id_d ,home_ine.ANOENC, home_ine.IMPEXACPSP 
			FROM home_ine where home_ine.impexacpsp <> '' and home_ine.IMPEXACPSP is not null) hogar ON gasto.id_d = hogar.id_d
WHERE CODIGO between '04511' and '04551'
group by 1,2;