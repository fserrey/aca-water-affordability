#import pandas as pd
import os, errno
import shutil

# This script will transform previous CSVs uploaded from PSPP

# 1 #
# Let's create all the directories where we will organise all the data

directory = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'epf_folder')

if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

directory_gastos = os.path.join(directory,'tablas_gastos')
directory_hogar = os.path.join(directory,'tablas_hogar')

if not os.path.exists(directory_gastos) and not os.path.exists(directory_hogar):
    try:
        os.makedirs(directory_gastos)
        os.makedirs(directory_hogar)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

current_folder_gastos = input('Escriba la carpeta que contine los archivos CSV correspondientes a GASTOS: ')
current_folder_hogar = input('Escriba la carpeta que contine los archivos CSV correspondientes a HOGAR: ')

# We create two comprehension lists with the following structure
"""for subdir, dirs, files in os.walk(os.path.expanduser('~')):
    listado = [os.path.join(subdir, i) for i in dirs]
    if current_folder_gastos in listado:
        src_gastos = os.path.join(subdir, i)
    elif current_folder_hogar in listado:
        src_hogar = os.path.join(subdir, i)
        """
src_gastos = [os.path.join(subdir, i) for subdir, dirs, files in os.walk(os.path.expanduser('~')) for i in dirs if current_folder_gastos in os.path.join(subdir, i)][0]
src_hogar = [os.path.join(subdir, i) for subdir, dirs, files in os.walk(os.path.expanduser('~')) for i in dirs if current_folder_hogar in os.path.join(subdir, i)][0]

filelist_gastos = os.listdir(src_gastos)
filelist_hogar = os.listdir(src_hogar)


# We are moving files from the previous directory to the ones we want (we aould avoid future Errors if we unify the address of the files)
try:
    for i in filelist_gastos:
        if i.endswith('.csv'):
            shutil.move(os.path.join(src_gastos,i), os.path.join(directory_gastos,i))
    for i in filelist_hogar:
        if i.endswith('.csv'):
            shutil.move(os.path.join(src_hogar,i), os.path.join(directory_hogar,i))
except (RuntimeError, TypeError, NameError) as e:
    print(e)


#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")        