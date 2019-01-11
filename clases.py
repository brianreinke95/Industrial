

class materia:
    def __init__(self, nombre, codigo, nivel, modo_cursada, carga_horaria_semanal, carga_horaria_total):
        self.nombre = nombre
        self.codigo = codigo
        self.nivel = nivel
        self.modo_cursada = modo_cursada
        self.carga_horaria_semanal = carga_horaria_semanal
        self.carga_horaria_total = carga_horaria_total
    

class alumno:
    def __init__(self, nombre, apellido, edad, legajo, especialidad, años_cursando):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.legajo = legajo
        self.especialidad = especialidad
        self.años_cursando = años_cursando
    def diccionario(self):
        return {
            'nombre': [self.nombre],
            'apellido': [self.apellido],
            'edad': [self.edad],
            'legajo': [self.legajo],
            'especialidad': [self.especialidad],
            'tiempo cursando': [self.años_cursando]
        }

class aprobadas:
    def __init__(self, obj_materia, obj_profesor, nota_final, nota_primer_parcial, nota_segundo_parcial):
        self.obj_materia = obj_materia
        self.obj_profesor = obj_profesor
        self.nota_final = nota_final
        self.nota_primer_parcial = nota_primer_parcial
        self.nota_segundo_parcial = nota_segundo_parcial

class final_pendiente:
    def __init__(self, obj_materia, obj_profesor, nota_primer_parcial, nota_segundo_parcial, fecha_finales):
        self.obj_materia = obj_materia
        self.obj_profesor = obj_profesor
        self.nota_primer_parcial = nota_primer_parcial
        self.nota_segundo_parcial = nota_segundo_parcial
        self.fecha_finales = fecha_finales

class por_cursar:
    def __init__(self, obj_materia, list_obj_profesores, horarios):
        self.obj_materia = obj_materia
        self.list_obj_profesores = list_obj_profesores
        self.horarios = horarios

class registro:
    def __init__(self, obj_alumno, list_obj_aprobadas, list_obj_final_pendiente, list_obj_por_cursar):
        self.obj_alumno = obj_alumno
        self.list_obj_aprobadas = list_obj_aprobadas
        self.list_obj_final_pendiente = list_obj_final_pendiente
        self.list_obj_por_cursar = list_obj_por_cursar
    def nro_aprobadas(self):
        return len(self.list_obj_aprobadas)
    def nro_finales_pendientes(self):
        return len(self.list_obj_final_pendiente)
    def nro_materias_por_cursar(self):
        return len(self.list_obj_por_cursar)
    def mostrar_aprobadas(self):
        for i in range(len(self.list_obj_aprobadas)):
            print(self.list_obj_aprobadas[i].nombre)
    def mostrar_finales_pendientes(self):
        for i in range(len(self.list_obj_final_pendiente)):
            print(self.list_obj_final_pendiente[i].nombre)
    def mostrar_por_cursar(self):
        for i in range(len(self.list_obj_por_cursar)):
            print(self.list_obj_por_cursar[i].nombre)




