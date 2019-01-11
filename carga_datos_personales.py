### Carga de datos personales.

from clases import alumno
import pandas as pd
import os.path

nombre = input('Ingresar nombre: ')
apellido = input('Ingresar apellido: ')
edad = int(input('Ingresar edad: '))
legajo = int(input('Ingresar legajo: '))
especialidad = input('Ingresar especialidad: ')
años_cursando = int(input('¿Cuántos años llevas cursando? '))


alumno1 = alumno(nombre=nombre, apellido=apellido, edad=edad, legajo=legajo, especialidad=especialidad,
                 años_cursando=años_cursando)

df = pd.DataFrame(alumno1.diccionario())
if os.path.isfile('alumnos.csv'):
    df.to_csv('alumnos.csv', index=False, sep=';', mode='a', header=False)
else:
    df.to_csv('alumnos.csv', index=False, sep=';')





print(df)