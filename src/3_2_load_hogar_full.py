import os
import pymysql

from dotenv import load_dotenv
load_dotenv()

hostname = os.environ["HOST_DO"]
username = os.environ["USERNAME_DO"]
password = os.environ["PASS_DO"]
database = os.environ["DATABASE_DO"] 
puerto = int(os.environ["PORT_DO"])

print("Using pymysql…")


con = pymysql.connect(hostname, username, 
    password, database, puerto)

with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))

query = """
        CREATE TABLE hogar_ine
        (
            id SERIAL,
            ACTESTB VARCHAR(10),
            ACTESTBRED VARCHAR(10),
            ACTESTB_RED VARCHAR(10),
            AGUACALI VARCHAR(10),
            AGUACV1 VARCHAR(10),
            AGUACV2 VARCHAR(10),
            AGUACV3 VARCHAR(10),
            AGUACV4 VARCHAR(10),
            AGUACV5 VARCHAR(10),
            AGUACV6 VARCHAR(10),
            AGUACV7 VARCHAR(10),
            AGUACV8 VARCHAR(10),
            AGUACV9 VARCHAR(10),
            ANNOCON VARCHAR(10),
            ANOENC INTEGER,
            CAJENA VARCHAR(10),
            CALEF VARCHAR(10),
            CALEFV1 VARCHAR(10),
            CALEFV2 VARCHAR(10),
            CALEFV3 VARCHAR(10),
            CALEFV4 VARCHAR(10),
            CALEFV5 VARCHAR(10),
            CALEFV6 VARCHAR(10),
            CALEFV7 VARCHAR(10),
            CALEFV8 VARCHAR(10),
            CALEFV9 VARCHAR(10),
            CAPROP VARCHAR(10),
            CAPROV VARCHAR(10),
            CCAA INTEGER,
            CLATEO VARCHAR(10),
            CLAVE VARCHAR(10),
            COMIHU VARCHAR(10),
            COMIINV VARCHAR(10),
            COMIMH VARCHAR(10),
            COMISD VARCHAR(10),
            COMITOT VARCHAR(10),
            CONTRATO VARCHAR(10),
            CONVIVENCIASP VARCHAR(10),
            DENSI VARCHAR(10),
            DENSIDAD VARCHAR(10),
            DESEM VARCHAR(10),
            DIASV1 VARCHAR(10),
            DIASV2 VARCHAR(10),
            DIASV3 VARCHAR(10),
            DIASV4 VARCHAR(10),
            DIASV5 VARCHAR(10),
            DIASV6 VARCHAR(10),
            DIASV7 VARCHAR(10),
            DIASV8 VARCHAR(10),
            DIASV9 VARCHAR(10),
            DISPOSIOV VARCHAR(10),
            DISPOSI_OV VARCHAR(10),
            ECIVILLEGALSP VARCHAR(10),
            ECIVILSP VARCHAR(10),
            EDADSP VARCHAR(10),
            ESTUDIOSSP VARCHAR(10),
            ESTUDIOS_SP VARCHAR(10),
            ESTUDREDSP VARCHAR(10),
            ESTUDRED_SP VARCHAR(10),
            FUENACV1 VARCHAR(10),
            FUENACV2 VARCHAR(10),
            FUENACV3 VARCHAR(10),
            FUENACV4 VARCHAR(10),
            FUENACV5 VARCHAR(10),
            FUENACV6 VARCHAR(10),
            FUENACV7 VARCHAR(10),
            FUENACV8 VARCHAR(10),
            FUENACV9 VARCHAR(10),
            FUENAGUA VARCHAR(10),
            FUENCALE VARCHAR(10),
            FUENCAV1 VARCHAR(10),
            FUENCAV2 VARCHAR(10),
            FUENCAV3 VARCHAR(10),
            FUENCAV4 VARCHAR(10),
            FUENCAV5 VARCHAR(10),
            FUENCAV6 VARCHAR(10),
            FUENCAV7 VARCHAR(10),
            FUENCAV8 VARCHAR(10),
            FUENCAV9 VARCHAR(10),
            FUENPRIN VARCHAR(10),
            FUENPRINRED VARCHAR(10),
            FUENPRIN_RED VARCHAR(10),
            GASTMON VARCHAR(20),
            GASTNOM1 VARCHAR(20),
            GASTNOM2 VARCHAR(20),
            GASTNOM3 VARCHAR(20),
            GASTNOM4 VARCHAR(20),
            GASTOT VARCHAR(20),
            IMPEXAC VARCHAR(10),
            IMPEXACPSP VARCHAR(10),
            IMPEXACP_SP VARCHAR(10),
            IMPUEXAC VARCHAR(10),
            IMPUEXACPSP VARCHAR(10),
            IMPUEXACP_SP VARCHAR(10),
            IMPUINTER VARCHAR(10),
            IMPUINTERPSP VARCHAR(10),
            IMPUTGAS VARCHAR(10),
            IMPU_INTER VARCHAR(10),
            IMPU_INTERPSP VARCHAR(10),
            INTERIN VARCHAR(10),
            INTERINPSP VARCHAR(10),
            INTERINP_SP VARCHAR(10),
            JORNADASP VARCHAR(10),
            MESESV1 VARCHAR(10),
            MESESV2 VARCHAR(10),
            MESESV3 VARCHAR(10),
            MESESV4 VARCHAR(10),
            MESESV5 VARCHAR(10),
            MESESV6 VARCHAR(10),
            MESESV7 VARCHAR(10),
            MESESV8 VARCHAR(10),
            MESESV9 VARCHAR(10),
            NACIONASP VARCHAR(10),
            NACIONA_SP VARCHAR(10),
            NACTOR VARCHAR(50),
            NHABIT VARCHAR(10),
            NHIJOSD VARCHAR(10),
            NMIEM1 VARCHAR(10),
            NMIEM10 VARCHAR(9),
            NMIEM11 VARCHAR(9),
            NMIEM12 VARCHAR(9),
            NMIEM13 VARCHAR(9),
            NMIEM2 VARCHAR(9),
            NMIEM3 VARCHAR(9),
            NMIEM4 VARCHAR(9),
            NMIEM5 VARCHAR(9),
            NMIEM6 VARCHAR(9),
            NMIEM7 VARCHAR(9),
            NMIEM8 VARCHAR(9),
            NMIEM9 VARCHAR(9),
            NMIEMB VARCHAR(9),
            NMIEMHU VARCHAR(10),
            NMIEMIN VARCHAR(10),
            NMIEMSD VARCHAR(10),
            NNINOSD VARCHAR(10),
            NORDENCOSP VARCHAR(10),
            NORDENCO_SP VARCHAR(10),
            NORDENMASP VARCHAR(10),
            NORDENMA_SP VARCHAR(10),
            NORDENPASP VARCHAR(10),
            NORDENPA_SP VARCHAR(10),
            NORDENSP VARCHAR(10),
            NUMACTI VARCHAR(10),
            NUMERO INTEGER,
            NUMESTU VARCHAR(10),
            NUMINACTI VARCHAR(10),
            NUMNOCUP VARCHAR(10),
            NUMNOESTU VARCHAR(10),
            NUMOCUP VARCHAR(10),
            NUMOVD VARCHAR(10),
            NUMPERI VARCHAR(10),
            NUTS1 VARCHAR(10),
            OCUPA VARCHAR(10),
            OCUPARED VARCHAR(10),
            OCUSP VARCHAR(10),
            OTROIN INTEGER,
            OTRSUB VARCHAR(10),
            PAISCODSP VARCHAR(9),
            PAISMADRESP VARCHAR(9),
            PAISNACODSP VARCHAR(9),
            PAISNACSP VARCHAR(9),
            PAISPADRESP VARCHAR(9),
            PAISSP VARCHAR(9),
            PENSIO VARCHAR(10),
            PERCEPSP VARCHAR(10),
            PF2RECO VARCHAR(10),
            PF2TEO VARCHAR(10),
            REGTEN VARCHAR(10),
            REGTENV1 VARCHAR(10),
            REGTENV2 VARCHAR(10),
            REGTENV3 VARCHAR(10),
            REGTENV4 VARCHAR(10),
            REGTENV5 VARCHAR(10),
            REGTENV6 VARCHAR(10),
            REGTENV7 VARCHAR(10),
            REGTENV8 VARCHAR(10),
            REGTENV9 VARCHAR(10),
            RENTAS VARCHAR(10),
            SECTOR VARCHAR(10),
            SEXOSP VARCHAR(10),
            SITPROF VARCHAR(10),
            SITSOCI VARCHAR(10),
            SITSOCIRE VARCHAR(10),
            SITSOCI_RE VARCHAR(10),
            SITUACTHOG VARCHAR(10),
            SITUACTSP VARCHAR(10),
            SITUACT_HOG VARCHAR(10),
            SITUACT_SP VARCHAR(10),
            SITUOCUHOG VARCHAR(10),
            SITUOCU_HOG VARCHAR(10),
            SITUREDSP VARCHAR(10),
            SITURED_SP VARCHAR(10),
            SITURESSP VARCHAR(10),
            SITURES_SP VARCHAR(10),
            SUPERF VARCHAR(10),
            TAMAMU VARCHAR(10),
            TAMANO VARCHAR(10),
            TIPHOGAR1 VARCHAR(9),
            TIPHOGAR10 VARCHAR(9),
            TIPHOGAR11 VARCHAR(9),
            TIPHOGAR2 VARCHAR(9),
            TIPHOGAR3 VARCHAR(9),
            TIPHOGAR4 VARCHAR(9),
            TIPHOGAR5 VARCHAR(9),
            TIPHOGAR6 VARCHAR(9),
            TIPHOGAR7 VARCHAR(9),
            TIPHOGAR8 VARCHAR(9),
            TIPHOGAR9 VARCHAR(9),
            TIPHOGAR_1 VARCHAR(9),
            TIPHOGAR_10 VARCHAR(9),
            TIPHOGAR_11 VARCHAR(9),
            TIPHOGAR_2 VARCHAR(9),
            TIPHOGAR_3 VARCHAR(9),
            TIPHOGAR_4 VARCHAR(9),
            TIPHOGAR_5 VARCHAR(9),
            TIPHOGAR_6 VARCHAR(9),
            TIPHOGAR_7 VARCHAR(9),
            TIPHOGAR_8 VARCHAR(9),
            TIPHOGAR_9 VARCHAR(9),
            TIPOCASA VARCHAR(9),
            TIPOCONT VARCHAR(9),
            TIPOEDIF VARCHAR(9),
            TRABAJO VARCHAR(9),
            UC1 VARCHAR(10),
            UC2 VARCHAR(10),
            UNIONSP VARCHAR(10),
            ZONARES VARCHAR(10),
            id_d VARCHAR(12),
            CONSTRAINT indicators_pkey PRIMARY KEY (id)
        ) """

con = pymysql.connect(hostname, username, 
    password, database)


with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))


conn = None
try:
    # We connect to the server
    conn = pymysql.connect(hostname, username, password, database)
    cur = conn.cursor()
    # We create the table
    cur.execute(query)
    # We close the connection
    cur.close()
    # Finally, we commit the changes
    conn.commit()
except (Exception, pymysql.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

directory_hogar = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_hogar')
filelist_hogar = os.listdir(directory_hogar)

for date in range(2006,2019):
    if date <2019:
        
        file_path = [os.path.join(directory_hogar,i) for i in filelist_hogar if f'{date}.csv' in i][0] 

        query = f"""
                LOAD DATA LOCAL INFILE '{file_path}'
                INTO TABLE hogar_ine 
                FIELDS TERMINATED BY ',' 
                LINES TERMINATED BY '\n' 
                IGNORE 1 ROWS 
                (ACTESTB, ACTESTBRED, ACTESTB_RED, AGUACALI, AGUACV1, AGUACV2, AGUACV3, AGUACV4, AGUACV5, AGUACV6, AGUACV7, AGUACV8, AGUACV9, ANNOCON, ANOENC, CAJENA, CALEF, CALEFV1, CALEFV2, CALEFV3, CALEFV4, CALEFV5, CALEFV6, CALEFV7, CALEFV8, CALEFV9, CAPROP, CAPROV, CCAA, CLATEO, CLAVE, COMIHU, COMIINV, COMIMH, COMISD, COMITOT, CONTRATO, CONVIVENCIASP, DENSI, DENSIDAD, DESEM, DIASV1, DIASV2, DIASV3, DIASV4, DIASV5, DIASV6, DIASV7, DIASV8, DIASV9, DISPOSIOV, DISPOSI_OV, ECIVILLEGALSP, ECIVILSP, EDADSP, ESTUDIOSSP, ESTUDIOS_SP, ESTUDREDSP, ESTUDRED_SP, FUENACV1, FUENACV2, FUENACV3, FUENACV4, FUENACV5, FUENACV6, FUENACV7, FUENACV8, FUENACV9, FUENAGUA, FUENCALE, FUENCAV1, FUENCAV2, FUENCAV3, FUENCAV4, FUENCAV5, FUENCAV6, FUENCAV7, FUENCAV8, FUENCAV9, FUENPRIN, FUENPRINRED, FUENPRIN_RED, GASTMON, GASTNOM1, GASTNOM2, GASTNOM3, GASTNOM4, GASTOT, IMPEXAC, IMPEXACPSP, IMPEXACP_SP, IMPUEXAC, IMPUEXACPSP, IMPUEXACP_SP, IMPUINTER, IMPUINTERPSP, IMPUTGAS, IMPU_INTER, IMPU_INTERPSP, INTERIN, INTERINPSP, INTERINP_SP, JORNADASP, MESESV1, MESESV2, MESESV3, MESESV4, MESESV5, MESESV6, MESESV7, MESESV8, MESESV9, NACIONASP, NACIONA_SP, NACTOR, NHABIT, NHIJOSD, NMIEM1, NMIEM10, NMIEM11, NMIEM12, NMIEM13, NMIEM2, NMIEM3, NMIEM4, NMIEM5, NMIEM6, NMIEM7, NMIEM8, NMIEM9, NMIEMB, NMIEMHU, NMIEMIN, NMIEMSD, NNINOSD, NORDENCOSP, NORDENCO_SP, NORDENMASP, NORDENMA_SP, NORDENPASP, NORDENPA_SP, NORDENSP, NUMACTI, NUMERO, NUMESTU, NUMINACTI, NUMNOCUP, NUMNOESTU, NUMOCUP, NUMOVD, NUMPERI, NUTS1, OCUPA, OCUPARED, OCUSP, OTROIN, OTRSUB, PAISCODSP, PAISMADRESP, PAISNACODSP, PAISNACSP, PAISPADRESP, PAISSP, PENSIO, PERCEPSP, PF2RECO, PF2TEO, REGTEN, REGTENV1, REGTENV2, REGTENV3, REGTENV4, REGTENV5, REGTENV6, REGTENV7, REGTENV8, REGTENV9, RENTAS, SECTOR, SEXOSP, SITPROF, SITSOCI, SITSOCIRE, SITSOCI_RE, SITUACTHOG, SITUACTSP, SITUACT_HOG, SITUACT_SP, SITUOCUHOG, SITUOCU_HOG, SITUREDSP, SITURED_SP, SITURESSP, SITURES_SP, SUPERF, TAMAMU, TAMANO, TIPHOGAR1, TIPHOGAR10, TIPHOGAR11, TIPHOGAR2, TIPHOGAR3, TIPHOGAR4, TIPHOGAR5, TIPHOGAR6, TIPHOGAR7, TIPHOGAR8, TIPHOGAR9, TIPHOGAR_1, TIPHOGAR_10, TIPHOGAR_11, TIPHOGAR_2, TIPHOGAR_3, TIPHOGAR_4, TIPHOGAR_5, TIPHOGAR_6, TIPHOGAR_7, TIPHOGAR_8, TIPHOGAR_9, TIPOCASA, TIPOCONT, TIPOEDIF, TRABAJO, UC1, UC2, UNIONSP, ZONARES, id_d);
                """
        conn = None
        try:
            conn = pymysql.connect(hostname, username, password, database, local_infile = 1)
            cur = conn.cursor()
            cur.execute(query)
            cur.close()
            conn.commit()
        except (Exception, pymysql.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
print('Tabla subida correctamente')

