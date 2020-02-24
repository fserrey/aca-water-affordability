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


# We create an load data for GASTOS

query = """
        CREATE TABLE gastos_ine
        (
            id SERIAL,
            ANOENC INTEGER NOT NULL,
            CANTIDAD VARCHAR(200), 
            CODIGO INTEGER, 
            GASTMON VARCHAR(200),
            GASTNOM1 VARCHAR(200),
            GASTNOM2 VARCHAR(200), 
            GASTNOM3 VARCHAR(200), 
            GASTNOM4 VARCHAR(200), 
            GASTNOM5 VARCHAR(200), 
            GASTO VARCHAR(200), 
            NACTOR VARCHAR(200),
            NUMERO INTEGER, 
            PORCEN VARCHAR(200), 
            PORCENDES VARCHAR(200), 
            PORCENIMP VARCHAR(200),
            id_d VARCHAR(200),
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

directory_gastos = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_gastos')
filelist_gastos = os.listdir(directory_gastos)

for date in range(2006,2019):
    if date <2019:
        file_path = [os.path.join(directory_gastos,i) for i in filelist_gastos if f'{date}.csv' in i]
        query = f"""
                LOAD DATA LOCAL INFILE '{file_path[0]}'
                INTO TABLE gastos_ine 
                FIELDS TERMINATED BY ',' 
                LINES TERMINATED BY '\n' 
                IGNORE 1 ROWS 
                (ANOENC, CANTIDAD, CODIGO, GASTMON, GASTNOM1, GASTNOM2, GASTNOM3, GASTNOM4, GASTNOM5, GASTO,NACTOR,NUMERO,PORCEN,PORCENDES,PORCENIMP, id_d);
                """
        conn = None
        try:
            conn = pymysql.connect(hostname, username, password, database, puerto, local_infile = 1)
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