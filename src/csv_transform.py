import pandas as pd
import os

# Clasificamos las variables de las tablas HOGAR en tipo int o float
# El fin de esto es poder distinguir a posteriori qué variables (columnas) son necesarias para cada
# una de las tablas. De este modo, unificamos el formato de todas (haciendo que los tres tipos de tabla
# tengan el mismo número de columnas)

file = 'hogar_2006.csv'
file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file
df = pd.read_csv(file_path)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_06 =  type_dct['float64']
int_hogar_06 = type_dct['int64']

file = 'hogar_2011.csv'
file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file
df = pd.read_csv(file_path)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_11 = type_dct['float64']
int_hogar_11 = type_dct['int64']

file = 'hogar_2016.csv'
file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file
df = pd.read_csv(file_path)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_16 = type_dct['float64']
int_hogar_16 = type_dct['int64']

# Distinguimos el conjunto de variables float e int que deberíamos añadir a cada tabla.

add_int_06 = [i for i in int_hogar_16 + int_hogar_11 if i not in int_hogar_06] 
add_int_11 = [i for i in int_hogar_06 + int_hogar_16 if i not in int_hogar_11] 
add_int_16 = [i for i in int_hogar_06 + int_hogar_11 if i not in int_hogar_16] 


add_float_06 = [i for i in float_hogar_16 + float_hogar_11 if i not in float_hogar_06] 
add_float_11 = [i for i in float_hogar_06 + float_hogar_16 if i not in float_hogar_11] 
add_float_16 = [i for i in float_hogar_06 + float_hogar_11 if i not in float_hogar_16]

# Creamos las variables que conforman el total de columnas necesarias para cada tabla

total_int_06 = int_hogar_06 + add_int_06
total_int_11 = int_hogar_11 + add_int_11
total_int_16 = int_hogar_16 + add_int_16

total_float_06 = float_hogar_06 + add_float_06
total_float_11 = float_hogar_11 + add_float_11
total_float_16 = float_hogar_16 + add_float_16

#actualización columnas 2006-2011
for date in range(2006,2011):
    if date <2011:
        file = f'hogar_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file

        id_d = 'id_d'
        df = pd.read_csv(file_path)

        columnas = [i for i in set(total_int_06+total_float_06) if i not in set(list(df.columns))] 

        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
            
        df_aux.to_csv(file_path, index=False)
#actualización de columnas 2011 - 2016
for date in range(2011,2016):
    if date <2016:
        file = f'hogar_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file

        id_d = 'id_d'

        df = pd.read_csv(file_path)

        columnas =  [i for i in set(total_int_11+total_float_11) if i not in set(list(df.columns))] 

        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        
        df_aux.to_csv(file_path, index=False)
#actualización de columnas 2016 - 2019

for date in range(2016,2019):
    if date <2019:
        file = f'hogar_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file
 
        id_d = 'id_d'
   
        df = pd.read_csv(file_path)

        columnas =  [i for i in set(total_int_16+total_float_16) if i not in set(list(df.columns))] 

        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        
        df_aux.to_csv(file_path, index=False)

# AÑADIENDO columna de ide primary key
for date in range(2006,2019):
    if date <2019:
        file = f'hogar_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/hogar/' + file
        
        df = pd.read_csv(file_path)
        print(date, len(df.columns))
        
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
            
        df.to_csv(file_path, index=False)
        print(date, len(df.columns))
print('Tablas hogar actualizadas')
for date in range(2006,2019):
    if date <2019:
        file = f'gastos_I_{date}.csv'
        file_path = '/home/fserrey/gitrep/ACA_project/aca-water-affordability/notebooks/dec_notebooks/gastos/' + file
        
        df = pd.read_csv(file_path)
        print(date, len(df.columns))
        
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
            
        df.to_csv(file_path, index=False)
        print(date, len(df.columns))
print('Tablas gastos actualizadas')

# Hemos terminado la transformación de los csv para subirlos al servidor MySQL
print("Has terminado la transformación de todas las tablas (por año)")
print("Ahora puedes utilizar server_uploaded para subir las tablas completas o select_server_upload para selección de columnas")