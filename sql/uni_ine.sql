USE aca_epf;
SELECT * FROM uni_ine;

SELECT ANOENC_x, SUM(IF(((GASTO/12)/IMPEXAC)*100 > 5, 1,0)) FLAG
FROM uni_ine
WHERE CODIGO IN('04411','04431')
group by 1;

SELECT ANOENC_x,  @rownum := COUNT(*) FROM uni_ine group by 1;

SELECT ANOENC_x, (SUM(IF(((GASTO/12)/IMPEXAC)*100 > 5, 1,0))/@rownum)*100 PORCENT
FROM uni_ine
WHERE CODIGO IN('04411','04431')
group by 1;