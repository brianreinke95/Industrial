from carga_materias import lista_obj_materias
from clases import *

list_obj_aprobadas = []
list_obj_final_pendiente = []
list_obj_por_cursar = []
condición = input('En este menpu se procederá a cargar el estado de las materias. ¿Quiere continuar? y->si n->no ')

if condición == 'y':
        i = 0
        for materia in lista_obj_materias:
            print(str(i)+': ' + materia.nombre)
            i += 1
        index = int(input('\n\n' + 'Seleccionar la materia (mediante su index) para cargar sus datos: '))
        print(lista_obj_materias[index])

        # Debo crear un loop que solo se salga si el usuario no quiere seguir cargando datos.
        # Debo visibilizar los datos que ya fueron cargados y si el usuario quiere modificar alguna materia
        # donde ya hay datos cargados mostrarlos y preguntarle si realmente quiere modificar los datos de la
        # misma.
        # Los objetos creados en este script deben ser guardados en un csv. Debo levantar los datos, crear un
        # dataframe, y analizar si ya existe algún objeto con el nombre de la materia seleccionada.
        # De existir, mensaje y opción. De no existir se le mostrará al usuario el nombre de la materia y
        # la no existencia de datos, y darle la opción de cargar datos en él o salir.

        # ¿Se podrá crear una ventana con el mensaje? Utilizar PyQt

        estado = input(lista_obj_materias[index].nombre + ', la tienes:\naprobada -> a\nfinal pendiente -> f\n'
                                                          'sin cursar->c\nRespuesta: ')
        if estado == 'a':
            nota_final = input('Nota final/promoción: ')
            nota_primer_parcial = input('Nota 1° parcial: ')
            nota_segundo_parcial = input('Nota 2° parcial: ')
            profesor = input('Profesor de cursada: ')
            list_obj_aprobadas.append(
                aprobadas(obj_materia=lista_obj_materias[index], nota_primer_parcial=nota_primer_parcial,
                          nota_segundo_parcial=nota_segundo_parcial, obj_profesor=profesor, nota_final=nota_final)
            )

        elif estado == 'f':
            nota_primer_parcial = input('Nota 1° parcial: ')
            nota_segundo_parcial = input('Nota 2° parcial: ')
            profesor = input('Profesor de cursada: ')
            list_obj_final_pendiente.append(
                final_pendiente(obj_materia=lista_obj_materias[index], nota_primer_parcial=nota_primer_parcial,
                          nota_segundo_parcial=nota_segundo_parcial, obj_profesor=profesor)
            )
        elif estado == 'c':
            list_obj_por_cursar.append(
                por_cursar(obj_materia=lista_obj_materias[index])
            )
        else:
            print('no ha seleccionado un item válido')


elif condición == 'n':
    print('aa')
else:
    print('Selección inválida, porfavor seleccione otra vez.')









'''
for i in range(len(lista_obj_materias)):
    print(lista_obj_materias[i])'''