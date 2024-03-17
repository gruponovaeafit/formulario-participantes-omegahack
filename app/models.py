from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), index=True)
    participantes = db.relationship('Participante', backref='equipo', lazy='dynamic')

    participantes = db.relationship('Participante', back_populates='equipo')

    def __repr__(self):
        return '<Equipo {}>'.format(self.nombre)

class Participante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    correo_institucional = db.Column(db.String(128), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)
    carrera = db.Column(db.String(128), nullable=False)
    sexo = db.Column(db.String(64), nullable=False)
    participacion_hackathon = db.Column(db.Boolean, default=False, nullable=False)
    tipo_inscripcion = db.Column(db.String(64), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=True)

    universidad = db.relationship('Universidad', backref='participantes')
    rol = db.relationship('Role', backref='participantes')
    equipo = db.relationship('Equipo', back_populates='participantes')

    def __repr__(self):
        return '<Participante {}>'.format(self.nombre)
    

class Universidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Universidad {}>'.format(self.nombre)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Role {}>'.format(self.nombre)
