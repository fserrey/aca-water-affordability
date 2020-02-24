import os
import pandas as pd
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

# seleccionamos las columnas que nos interesan

# Columnas que nos interesan

col_hogar = """ANOENC
NUMERO
CCAA
TAMAMU
DENSIDAD
FACTOR
NMIEMB
TAMAÑO
NUMACTI
NUMINACTI
NUMOCU
NUMNOCU
NUMESTU
NUMNOESTU
UC1
UC2
NORDENSP
EDADSP
SEXOSP
PAISNACSP
NACIONASP
PAISSP
CONVIVENCIASP
PAISPADRESP
PAISMADRESP
ESTUDREDSP
SITUREDSP
OCUSP
IMPEXACPSP
IMPEXAC
INTERINPSP
ACTESTBRED
SITPROF
TIPOCONT
REGTEN
TIPOEDIF
ZONARES
TIPOCASA
ANNOCON
AGUACALI
FUENAGUA
CALEF
FUENCALE
id_d"""

col_gasto = """ANOENC
CANTIDAD
CODIGO
GASTO
NACTOR
id_d"""

columnas_hogar = col_hogar.split("\n")
columnas_gastos = col_gasto.split("\n") 

# Creamos un nuevo directorio en el que almacenar estos datos y ejecutamos esta sección del código
for date in range(2006,2019):
    if date <2019:
        
        #Importamos csv de HOGAR y sacamos columnas que queremos
        file = f'hogar_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file

        
        df_hogar = pd.read_csv(file_path)
        df_hogar= df_hogar[df_hogar.columns.intersection(columnas_hogar)] # Con esto seleccionamos solo las columnas presentes en la lista
        
        #Importamos csv GASTOS y sacamos las columnas que queremos
        file = f'gastos_I_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/gastos/' + file

        
        df_gastos = pd.read_csv(file_path)
        df_gastos= df_gastos[df_gastos.columns.intersection(columnas_gastos)] # Con esto seleccionamos solo las columnas presentes en la lista
        
        #Hacemos un JOIN de las dos tablas
        df = df_hogar.merge(df_gastos, on='id_d', how='left')
        
        #Guardamos el csv con columnas unidas
        df.to_csv('/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/uni/' + f'uni_{date}.csv', index=False)

query = """
        CREATE TABLE uni_ine
        (
            id SERIAL,
            ACTESTBRED VARCHAR(200), 
            AGUACALI VARCHAR(200), 
            ANNOCON VARCHAR(200), 
            ANOENC_x INTEGER, 
            CALEF VARCHAR(200), 
            CCAA INTEGER, 
            CONVIVENCIASP VARCHAR(200), 
            DENSIDAD VARCHAR(200), 
            EDADSP VARCHAR(200), 
            ESTUDREDSP VARCHAR(200), 
            FUENAGUA VARCHAR(200), 
            FUENCALE VARCHAR(200), 
            IMPEXAC VARCHAR(200), 
            IMPEXACPSP VARCHAR(200), 
            INTERINPSP VARCHAR(200), 
            NACIONASP VARCHAR(200), 
            NMIEMB VARCHAR(200), 
            NORDENSP VARCHAR(200), 
            NUMACTI VARCHAR(200), 
            NUMERO VARCHAR(200), 
            NUMESTU VARCHAR(200), 
            NUMINACTI VARCHAR(200), 
            NUMNOESTU VARCHAR(200), 
            OCUSP VARCHAR(200), 
            PAISMADRESP VARCHAR(200), 
            PAISNACSP VARCHAR(200), 
            PAISPADRESP VARCHAR(200), 
            PAISSP VARCHAR(200), 
            REGTEN VARCHAR(200), 
            SEXOSP VARCHAR(200), 
            SITPROF VARCHAR(200), 
            SITUREDSP VARCHAR(200), 
            TAMAMU VARCHAR(200), 
            TIPOCASA VARCHAR(200), 
            TIPOCONT VARCHAR(200), 
            TIPOEDIF VARCHAR(200), 
            UC1 VARCHAR(200), 
            UC2 VARCHAR(200), 
            ZONARES VARCHAR(200), 
            id_d INTEGER, 
            ANOENC_y INTEGER, 
            CANTIDAD VARCHAR(200), 
            CODIGO INTEGER, 
            GASTO FLOAT, 
            NACTOR VARCHAR(200),
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
    # We connect to the PostgreSQL server
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
print('finished')

for date in range(2006,2019):
    if date <2019:
        file = f'uni_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/uni/' + file

        query = f"""
                LOAD DATA LOCAL INFILE '{file_path}'
                INTO TABLE uni_ine 
                FIELDS TERMINATED BY ',' 
                LINES TERMINATED BY '\n' 
                IGNORE 1 ROWS 
                (ACTESTBRED, AGUACALI, ANNOCON, ANOENC_x, CALEF, CCAA, CONVIVENCIASP, DENSIDAD, EDADSP, ESTUDREDSP, FUENAGUA, FUENCALE, IMPEXAC, IMPEXACPSP, INTERINPSP, NACIONASP, NMIEMB, NORDENSP, NUMACTI, NUMERO, NUMESTU, NUMINACTI, NUMNOESTU, OCUSP, PAISMADRESP, PAISNACSP, PAISPADRESP, PAISSP, REGTEN, SEXOSP, SITPROF, SITUREDSP, TAMAMU, TIPOCASA, TIPOCONT, TIPOEDIF, UC1, UC2, ZONARES, id_d, ANOENC_y, CANTIDAD, CODIGO, GASTO, NACTOR)"""
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