import pandas as pd
import os, errno

# This file will normalize/Transform tables format in order to make it feasible to upload them to our DB

# INE microdata format and features have changed over time. INE states 3 different types:
## From 2006 to 2010
## From 2011 to 2015
## From 2016 till NOW (2020)

# It's importat that all our tables has same format and shape

#############################################################################

# We first classify our features in FLOAT or INT

directory_hogar = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_hogar')
filelist_hogar = os.listdir(directory_hogar)


file_06 = [os.path.join(directory_hogar,i) for i in filelist_hogar if '2006.csv' in i][0]

df = pd.read_csv(file_06)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_06 =  type_dct['float64']
int_hogar_06 = type_dct['int64']


file_11 = [os.path.join(directory_hogar,i) for i in filelist_hogar if '2011.csv' in i][0]

df = pd.read_csv(file_11)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_11 = type_dct['float64']
int_hogar_11 = type_dct['int64']


file_16 = [os.path.join(directory_hogar,i) for i in filelist_hogar if '2016.csv' in i][0]

df = pd.read_csv(file_16)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_hogar_16 = type_dct['float64']
int_hogar_16 = type_dct['int64']

# For both IN and FLOAT we filter by all features that are needed in each group of files

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

# If INE change the grupos again, just add a new elif and move the range for the else

for date in range(2006,2019):
    if date <2011:
        file_path = [os.path.join(directory_hogar,i) for i in filelist_hogar if f'{date}.csv' in i]      
        df = pd.read_csv(file_path[0])
        columnas = [i for i in set(total_int_06+total_float_06) if i not in set(list(df.columns))]
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'hogar_epf_{date}.csv'), index=False)
    
    elif date in range(2011,2016):
        file_path = [os.path.join(directory_hogar,i) for i in filelist_hogar if f'{date}.csv' in i]        
        df = pd.read_csv(file_path[0])
        columnas =  [i for i in set(total_int_11+total_float_11) if i not in set(list(df.columns))]  
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'hogar_epf_{date}.csv'), index=False)
    
    else:
        file_path = [os.path.join(directory_hogar,i) for i in filelist_hogar if f'{date}.csv' in i]        
        df = pd.read_csv(file_path[0])
        columnas =  [i for i in set(total_int_16+total_float_16) if i not in set(list(df.columns))]  
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'hogar_epf_{date}.csv'), index=False)
##################################################################################################

# We now do the same with GASTOS
directory_gastos = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder', 'tablas_gastos')
filelist_gastos = os.listdir(directory_gastos)


file_06 = [os.path.join(directory_gastos,i) for i in filelist_gastos if '2006.csv' in i][0]

df = pd.read_csv(file_06)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_gastos_06 =  type_dct['float64']
int_gastos_06 = type_dct['int64']


file_11 = [os.path.join(directory_gastos,i) for i in filelist_gastos if '2011.csv' in i][0]

df = pd.read_csv(file_11)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_gastos_11 = type_dct['float64']
int_gastos_11 = type_dct['int64']


file_16 = [os.path.join(directory_gastos,i) for i in filelist_gastos if '2016.csv' in i][0]

df = pd.read_csv(file_16)
type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}
float_gastos_16 = type_dct['float64']
int_gastos_16 = type_dct['int64']

# For both IN and FLOAT we filter by all features that are needed in each group of files

add_int_06 = [i for i in int_gastos_16 + int_gastos_11 if i not in int_gastos_06] 
add_int_11 = [i for i in int_gastos_06 + int_gastos_16 if i not in int_gastos_11] 
add_int_16 = [i for i in int_gastos_06 + int_gastos_11 if i not in int_gastos_16] 


add_float_06 = [i for i in float_gastos_16 + float_gastos_11 if i not in float_gastos_06] 
add_float_11 = [i for i in float_gastos_06 + float_gastos_16 if i not in float_gastos_11] 
add_float_16 = [i for i in float_gastos_06 + float_gastos_11 if i not in float_gastos_16]

# Creamos las variables que conforman el total de columnas necesarias para cada tabla

total_int_06 = int_gastos_06 + add_int_06
total_int_11 = int_gastos_11 + add_int_11
total_int_16 = int_gastos_16 + add_int_16

total_float_06 = float_gastos_06 + add_float_06
total_float_11 = float_gastos_11 + add_float_11
total_float_16 = float_gastos_16 + add_float_16

# If INE change the grupos again, just add a new elif and move the range for the else

for date in range(2006,2019):
    if date <2011:
        file_path = [os.path.join(directory_gastos,i) for i in filelist_gastos if f'{date}.csv' in i]        
        df = pd.read_csv(file_path[0])
        columnas = [i for i in set(total_int_06+total_float_06) if i not in set(list(df.columns))]
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'gastos_epf_{date}.csv'), index=False)
    
    elif date in range(2011,2016):
        file_path = [os.path.join(directory_gastos,i) for i in filelist_gastos if f'{date}.csv' in i]        
        df = pd.read_csv(file_path[0])
        columnas =  [i for i in set(total_int_11+total_float_11) if i not in set(list(df.columns))]  
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'gastos_epf_{date}.csv'), index=False)
    
    else:
        file_path = [os.path.join(directory_gastos,i) for i in filelist_gastos if f'{date}.csv' in i]        
        df = pd.read_csv(file_path[0])
        columnas =  [i for i in set(total_int_16+total_float_16) if i not in set(list(df.columns))]  
        df_aux = pd.concat([df,pd.DataFrame(columns=columnas)], sort=True)
        df["id_d"] = df["ANOENC"].astype(int).astype(str) + df["NUMERO"].astype(int).astype(str) 
        df_aux.to_csv(os.path.join(os.path.dirname(file_path[0]),f'gastos_epf_{date}.csv'), index=False)
    


# Hemos terminado la transformación de los csv para subirlos al servidor MySQL
print("Has terminado la transformación de todas las tablas (por año)")
print("Ahora puedes utilizar server_uploaded para subir las tablas completas o select_server_upload para selección de columnas")