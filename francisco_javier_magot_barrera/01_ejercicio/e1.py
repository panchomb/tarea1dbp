import psycopg2

connection = psycopg2.connect('dbname=ejercicio1db user=postgres password=negrito4')

cursor = connection.cursor()

cursor.execute('drop table if exists profesor cascade;')
cursor.execute('''
    create table profesor(
        id int primary key,
        nombre varchar(50),
        apellido varchar,
        edad int,
        sexo varchar(10)
    );
''')

cursor.execute('drop table if exists curso cascade;')
cursor.execute('''
    create table curso(
        id int primary key,
        nombre varchar(50),
        creditos int,
        horas int,
        carrera varchar(50)
    );
''')

cursor.execute('drop table if exists seccion cascade;')
cursor.execute('''
    create table seccion(
        id int primary key,
        nombre varchar(50),
        curso_id int references curso(id),
        profesor_id int,
        num_clase int
    );
''')

cursor.execute('drop table if exists estudiante cascade;')
cursor.execute('''
    create table estudiante(
        id int primary key,
        nombre varchar(50),
        apellido varchar(50),
        edad int,
        seccion_id int references seccion(id)
    );
''')




cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (1, 'DBP', 2, 3, 'CS');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (2, 'Matematicas 3', 4, 5, 'Todas');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (3, 'Estadistica', 4, 5, 'Todas');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (4, 'POO 2', 4, 5, 'CS');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (5, 'Arquitectura de Computadoras', 3, 4, 'CS');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (6, 'PI 1', 2, 2, 'Todas');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (7, 'Estructuras Discretas 2', 4, 6, 'CS');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (8, 'Fisica 2', 4, 4, 'Todas');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (9, 'Gestion de Empresas', 2, 3, 'Todas');")
cursor.execute("insert into curso(id, nombre, creditos, horas, carrera) values (10, 'Comunicacion', 3, 4, 'Todas');")


cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (1, 'Ruben', 'Rivas', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (2, 'Talia', 'Tijero', 30, 'Mujer');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (3, 'Royer', 'Rojas', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (4, 'Marvin', 'Abisrror', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (5, 'Jorge', 'Reanio', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (6, 'Hermes', 'Pantoja', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (7, 'Brigida', 'Molina', 30, 'Mujer');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (8, 'Yamilet', 'Serrano', 30, 'Mujer');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (9, 'Carlos', 'Guevara', 30, 'Hombre');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (10, 'Katia', 'Zegarra', 30, 'Mujer');")
cursor.execute("insert into profesor(id, nombre, apellido, edad, sexo) values (11, 'Teresa', 'Toreres', 30, 'Mujer');")

cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (1, 'Lab 1.01', 5, 5, 70);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (2, 'Lab 1.01', 1, 4, 32);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (3, 'Lab 4.01', 3, 3, 80);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (4, 'Lab 1', 2, 7, 17);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (5, 'Teoria 1.01', 2, 6, 52);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (6, 'Lab 2.01', 4, 1, 27);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (7, 'Teoria 7', 6, 2, 72);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (8, 'Lab 3.01', 10, 11, 50);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (9, 'Lab 1.01', 9, 9, 48);")
cursor.execute("insert into seccion(id, nombre, curso_id, profesor_id, num_clase) values (10, 'Lab 3.01', 8, 10, 1);")

cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 1, 'Francisco', 'Magot', 19, 1)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 2, 'Sebastian', 'Chu', 19, 7)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 3, 'Rodrigo', 'Gomez', 20, 5)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 4, 'Alvaro', 'Villena', 18, 4)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 5, 'Vicente', 'Pastor', 17, 4)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 6, 'Mauricio', 'Croquet', 18, 3)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 7, 'Sebastian', 'Chu', 18, 10)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 8, 'Dario', 'Blanco', 20, 6)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 9, 'Nicolas', 'Orezzoli', 17, 2)")
cursor.execute("insert into estudiante(id, nombre, apellido, edad, seccion_id) values ( 10, 'Patrick', 'Sparks', 19, 8)")

cursor.execute("select * from curso;")
rows = cursor.fetchall()
print("Cursos: ")
for row in rows:
    print(row)
print('\n')

cursor.execute("select * from profesor;")
rows = cursor.fetchall()
print("Profesores: ")
for row in rows:
    print(row)
print('\n')

cursor.execute("select * from seccion;")
rows = cursor.fetchall()
print("Secciones: ")
for row in rows:
    print(row)
print('\n')

cursor.execute("select * from estudiante;")
rows = cursor.fetchall()
print("Estudiantes: ")
for row in rows:
    print(row)
print('\n')

connection.commit()
connection.close()

cursor.close()