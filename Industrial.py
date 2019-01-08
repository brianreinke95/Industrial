import pandas as pd
import re
from functools import reduce
import numpy as np

desired_width = 1000
pd.set_option("display.max_columns", 12)
pd.set_option("display.max_rows", 100)
pd.set_option('display.width', desired_width)
pd.set_option('display.colheader_justify', 'right')

url = r"C:\Users\brian\Desktop\Industrial.xlsx"
df = pd.read_excel(url, usecols='A:F', header=None, skiprows=2,
                   names=['Nivel', 'Código', 'Nombre', 'Cuatrimestral/Anual', 'Carga Horaria Semanal',
                          'Carga Horaria Total'])


df['Nivel'].fillna(method='ffill', inplace=True)

df.set_index('Nivel', inplace=True)



''' Puedo separar en varios dataframes distintos con gropus by, los agrupo en una lista.'''
''' Se puede descartar las filas '''
df_list = []
g = df.groupby('Nivel')
for index, index_df in g:
    if re.search(r'\dº', index) or re.search(r'ELEC', index):
        df_list.append(index_df)



# Concateno todos los dataFrames para modificar el original y obtener un DataFrame limpio.
df = reduce(lambda x, y: pd.concat([x, y]), df_list)

# Sustraigo la carga horaria total por año en otro dataFrame
carga_horaria_por_año = df[df['Código'] == 'Carga horaria total:']
carga_horaria_por_año = carga_horaria_por_año.drop(columns=['Nombre', 'Cuatrimestral/Anual', 'Código'])

# Me quedo con la tabla que no contiene a lo anterior:
df = df[df['Código'] != 'Carga horaria total:']

''' Para este caso podría copiar lo de arriba (ffill) y luego agruparlo'''
df.fillna(method='ffill', inplace=True)


aux = df.loc[df['Cuatrimestral/Anual'] == 'Cuatrimestral / Anual']
aux = aux.astype({'Carga Horaria Semanal': str})  # Cambio el tipo de dato de toda la columna para conseguir strings
# Esto para poder encontrar ambas coincidencias en una sola regex.

a = aux['Carga Horaria Semanal'].values
value = a[0] + ' ' + a[1]               # para este tipos de casos la fila siguiente tendrá lo que le falta.

# Hago que ambas filas sean iguales para luego eliminar 1 de ellas.
aux = aux.replace({
    'Carga Horaria Semanal': '/? ?\d'
}, value, regex=True)

df.loc[df['Cuatrimestral/Anual'] == 'Cuatrimestral / Anual'] = aux  # Modifico el original con lo modificado.
df = df.drop_duplicates()


#print(df)
#print(carga_horaria_por_año)


