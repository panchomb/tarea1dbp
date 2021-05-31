from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:negrito4@localhost:5432/ejercicio3db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Orden(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key = True)
    destino = db.Column(db.String(50), nullable = False)
    productos = db.Column(db.String(100), nullable = False)
    vehiculo = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f'<Orden: {self.id}, {self.destino}, {self.productos}, {self.vehiculo}>'

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(50), nullable = False)
    pedido = db.Column(db.String(100))

    def __repr__(self):
        return f'<Usuario: {self.id}, {self.user}, {self.pedido}>'


db.create_all()

@app.route('/')
def index():
    return render_template('index.html',
        ordenes = Orden.query.all(),
        usuarios = Usuario.query.all()
    )

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug=True)