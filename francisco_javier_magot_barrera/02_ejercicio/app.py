from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://panchomb:1234@localhost:3306/ejercicio2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Profesor(db.Model):
    __tablename__ = 'profesor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable = False)
    apellido = db.Column(db.String(80), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    sexo = db.Column(db.String(80), nullable = False)
    secciones = db.relationship('Seccion', backref = 'profesor')

    def __repr__(self):
        return f'<Profesor: {self.id}, {self.nombre}, {self.apellido}, {self.edad}, {self.sexo}>'

clases = db.Table('clases',
    db.Column('alumno_id', db.Integer, db.ForeignKey('estudiante.id')),
    db.Column('seccion_id', db.Integer, db.ForeignKey('seccion.id'))
)

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    codigo = db.Column(db.Integer, nullable = False)
    secs = db.relationship('Seccion', secondary = clases, backref=db.backref('estudiantes', lazy = 'dynamic'))

    def __repr__(self):
        return f'<Estudiante: {self.id}, {self.nombre}, {self.apellido}, {self.edad}, {self.codigo}>'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    creditos = db.Column(db.Integer, nullable = False)
    horas = db.Column(db.Integer, nullable = False)
    carrera = db.Column(db.String(50), nullable = False)
    secciones = db.relationship('Seccion', backref='curso')

    def __repr__(self):
        return f'<Curso: {self.id}, {self.nombre}, {self.creditos}, {self.horas}, {self.carrera}>'

class Seccion(db.Model):
    __tablename__ = 'seccion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable = False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'), nullable = False)
    num_clase = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'<Seccion: {self.id}, {self.nombre}, {self.curso_id}, {self.profesor_id}, {self.num_clase}>'


   

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', cursos = Curso.query.all(), profesores = Profesor.query.all(), estudiantes = Estudiante.query.all(), secciones = Seccion.query.all())




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002, debug=True)
