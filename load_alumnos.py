from clases import *
import pandas as pd
import os
pd.set_option("display.max_columns", 12)

try:
    df = pd.read_csv('alumnos.csv', sep=';')
except FileNotFoundError:
    os._exit(1)

list_obj_alumnos = []

for index, row in df.iterrows():
    list_obj_alumnos.append(
        alumno(nombre=row['nombre'], apellido=row['apellido'], edad=row['edad'], legajo=row['legajo'],
           especialidad=row['especialidad'], años_cursando=row['tiempo cursando']))


