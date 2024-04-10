from app import db
from datetime import datetime

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), index=True)
    participantes_seleccionados = db.relationship('ParticipanteSeleccionado', backref='equipo', lazy='dynamic')

    participantes_seleccionados = db.relationship('ParticipanteSeleccionado', back_populates='equipo')

    def __repr__(self):
        return '<Equipo {}>'.format(self.nombre)
    

class ParticipanteSeleccionado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    correo_institucional = db.Column(db.String(128), unique=True, nullable=False)
    tipo_inscripcion = db.Column(db.String(64), nullable=False)
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    participante = db.relationship('Participante', back_populates='participante_seleccionado')

    universidad = db.relationship('Universidad', backref='participantes_seleccionados')
    rol = db.relationship('Role', backref='participantes_seleccionados')
    equipo = db.relationship('Equipo', back_populates='participantes_seleccionados')

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
    

class Participante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer, nullable=False)
    eps = db.Column(db.String(128), nullable=False)
    contacto_emergencia = db.Column(db.String(128), nullable=False)
    parentesco_contacto_emergencia = db.Column(db.String(128), nullable=False)
    alergias = db.Column(db.String(255), nullable=False)
    enfermedades = db.Column(db.String(255), nullable=False)
    numero_contacto_emergencia = db.Column(db.String(128), nullable=False)
    tratamiento_datos = db.Column(db.Boolean, nullable=False)
    seguridad_asistencia = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    id_participante_seleccionado = db.Column(db.Integer, db.ForeignKey('participante_seleccionado.id'), nullable=False)

    participante_seleccionado = db.relationship('ParticipanteSeleccionado', back_populates='participante')

    def __repr__(self):
        return '<Participante {}>'.format(self.id)
