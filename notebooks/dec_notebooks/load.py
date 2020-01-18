import os
import pandas as pd
import pyreadstat
import glob
from functools import wraps
from time import time
import savReaderWriter as spss

def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper

#Funciones GASTOS
@timer
def get_tablas_gastos(base_dir):
    for file in os.listdir(base_dir):
        file_path = f'{base_dir}/{file}'
        
        raw_data = spss.SavReader(file_path, returnHeader = True)
        raw_data_list = list(raw_data)
        df = pd.DataFrame(raw_data_list)
        display(df.head(3))
        
        df = df.apply(lambda x: x.astype(float)/100 if x.name not in ['ANOENC', 'NUMERO','CODIGO', 'NACTOR'] else x)
        df = df.apply(lambda x: x.astype(int) if x.name in ['ANOENC', 'NUMERO'] else x)
        df = df.apply(lambda x: x/1000000 if x.name in ['NACTOR'] else x)
        df.to_csv(base_dir+'/gastos_'+ str(df.iloc[0][0]) + '.csv')        

def setup(df):
    df = df.apply(lambda x: x.astype(float)/100 if x.name not in ['ANOENC', 'NUMERO','CODIGO', 'NACTOR'] else x)
    df = df.apply(lambda x: x.astype(int) if x.name in ['ANOENC', 'NUMERO'] else x)
    df = df.apply(lambda x: x/1000000 if x.name in ['NACTOR'] else x)
    return df

@timer
def load_tablas_gastos(base_dir):
    all_files = glob.glob(base_dir + "/*.csv")
    
    li = []
    for fname in all_files:
        df = pd.read_csv(fname, index_col=None, header=0)
        df = setup(df)
        li.append(df)

    dframe = pd.concat(li, axis=0, ignore_index=True) 
    dframe.to_csv('gastos_serie_completa.csv')
    


#Funciones HOGAR
@timer
def get_tablas_hogar(base_dir):
    for file in os.listdir(base_dir):
        file_path = f'{base_dir}/{file}'
        df, meta = pyreadstat.read_sav(file_path)
        df.to_csv(base_dir+'/hogar_'+ str(df.loc[0, "ANOENC"]) + '.csv')

@timer
def load_tablas_hogar(base_dir):
    all_files = glob.glob(base_dir + "/*.csv")
    
    li = []
    for fname in all_files:
        df = pd.read_csv(fname, index_col=None, header=0)
        li.append(df)

    dframe = pd.concat(li, axis=0, ignore_index=True) 
    dframe.to_csv('hogar_serie_completa.csv')

def validity(df_gastos, df_hogar):
    return df_gastos.shape == df_hogar.shape

ruta = "/home/fserrey/gitrep/ACA_project/docs_table/gastos_tablas"
load_tablas_gastos(ruta)