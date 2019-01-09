from Industrial import df
from clases import *

materias = df['Nombre'].values
materias = materias.tolist()
nivel = df.index.values.tolist()
codigo = df.loc[:, 'Código'].values.tolist()
modo_cursada = df.loc[:, 'Cuatrimestral/Anual'].values.tolist()
carga_horaria_semanal = df.loc[:, 'Carga Horaria Semanal'].values.tolist()
carga_horaria_total = df.loc[:, 'Carga Horaria Total'].values.tolist()

lista_obj_materias = []

# Creación de todos los objetos 'materia'. Agrupados en una lista.
for i in range(len(materias)):
    lista_obj_materias.append(materia(materias[i], codigo[i], nivel[i], modo_cursada[i],
                                      carga_horaria_semanal[i], carga_horaria_total[i]))

### Necesito que la gente se registre con un usuario y contraseña que le permita acceso a sus datos.
### Debo configurar permisos.
### Un menú donde las opciones sean cargar datos personales, cargar y modificar datos de las materias.
### Un apartado donde se pueda buscar los profesores, programa, horarios, etc a partir de la materia en específico.
### Cada profesor y materia tendrán una sección de comentarios y encuestas. También se tendrá un repositorio de
### parciales y finales los cuales tendrán referencias a las materias, al año y al profesor en cuestión.
### Debe haber una sección con gráficas y estadísticas sobre el progreso del estudiante.



### Carga de datos de materias.


'''
for i in range(len(lista_obj_materias)):
    print(lista_obj_materias[i].nombre)'''
'''
for i in range(len(lista_obj_materias)):
    print(str(lista_obj_materias[i]))'''
