import os
import pymysql
import pandas as pd

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

# We state the columns we are working with
columnas_hogar = ['ANOENC', 'NUMERO', 'CCAA', 'TAMAMU', 'DENSIDAD', 'FACTOR', 'NMIEMB', 'TAMAÑO', 'NUMACTI', 'NUMINACTI', 'NUMOCU', 'NUMNOCU', 'NUMESTU', 'NUMNOESTU', 'UC1', 'UC2', 'NORDENSP', 'EDADSP', 'SEXOSP', 'PAISNACSP', 'NACIONASP', 'PAISSP', 'CONVIVENCIASP', 'PAISPADRESP', 'PAISMADRESP', 'ESTUDREDSP', 'SITUREDSP', 'OCUSP', 'IMPEXACPSP', 'IMPEXAC', 'INTERINPSP', 'ACTESTBRED', 'SITPROF', 'TIPOCONT', 'REGTEN', 'TIPOEDIF', 'ZONARES', 'TIPOCASA', 'ANNOCON', 'AGUACALI', 'FUENAGUA', 'CALEF', 'FUENCALE', 'id_d']
columnas_gastos = ['ANOENC', 'CANTIDAD', 'CODIGO', 'GASTO', 'NACTOR', 'id_d']

# we are including those columns as defaul, but we are open if someone want to add some more

print('Para esta tabla hemos preseleccionado estas variables por defecto de HOGAR: ', columnas_hogar)
to_add_hogar = input('¿Quieres añadir alguna más? ')

print('Para esta tabla hemos preseleccionado estas variables por defecto de GASTOS: ', columnas_gastos)
to_add_gastos = input('¿Quieres añadir alguna más? ')


directory_hogar = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_hogar')
filelist_hogar = os.listdir(directory_hogar)

directory_gastos = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_gastos')
filelist_gastos = os.listdir(directory_gastos)


for date in range(2006,2019):
    if date <2019:
        
        #Importamos csv de HOGAR y sacamos columnas que queremos
        file_path = [os.path.join(directory_hogar,i) for i in filelist_hogar if f'{date}.csv' in i]
        
        df_hogar = pd.read_csv(file_path[0])
        df_hogar= df_hogar[df_hogar.columns.intersection(columnas_hogar)] # Con esto seleccionamos solo las columnas presentes en la lista
        
        #Importamos csv GASTOS y sacamos las columnas que queremos
        file_path = [os.path.join(directory_gastos,i) for i in filelist_gastos if f'{date}.csv' in i]
        
        df_gastos = pd.read_csv(file_path[0])
        df_gastos= df_gastos[df_gastos.columns.intersection(columnas_gastos)] # Con esto seleccionamos solo las columnas presentes en la lista
        
        #Hacemos un JOIN de las dos tablas
        df = df_hogar.merge(df_gastos, on='id_d', how='left')
        
        #Guardamos el csv con columnas unidas
        directory = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_filtradas')

        if not os.path.exists(directory):
            try:
                filtrados = os.makedirs(os.path.join(directory))
                df.to_csv(os.path.join(filtrados, f'uni_{date}.csv'), index=False)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

directory_fil = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_gastos')
filelist_fil = os.listdir(directory_fil)

file_path = [os.path.join(directory_fil,i) for i in filelist_fil if '2018.csv' in i][0]
df = pd.read_csv(file_path) 
variables = list(df.columns )

features = []
for i in variables:
    if i in ('ANOENC_x', 'CCAA', 'id_d', 'ANOENC_y', 'CANTIDAD', 'CODIGO'):
        features.append(i + ' INTEGER, ')
    elif i in ('GASTO'):
        features.append(i + ' FLOAT, ')
    else:
        features.append(i + ' VARCHAR(200), ')
    
features_query_1 = ''.join(features)
features_query_2 = ', '.join(variables)


query = """CREATE TABLE uni_ine (id SERIAL,""" + features_query_1 + """, CONSTRAINT indicators_pkey PRIMARY KEY (id))"""

conn = None
try:
    conn = pymysql.connect(hostname, username, password, database)
    cur = conn.cursor()
    cur.execute(query)
    cur.close()
    conn.commit()
except (Exception, pymysql.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
print('table created')


for date in range(2006,2019):
    if date <2019:
        file_path = [os.path.join(directory_fil,i) for i in filelist_fil if f'{date}.csv' in i][0]
        query = f"""
                LOAD DATA LOCAL INFILE '{file_path}'
                INTO TABLE uni_ine 
                FIELDS TERMINATED BY ',' 
                LINES TERMINATED BY '\n' 
                IGNORE 1 ROWS 
                ({features_query_2})"""
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