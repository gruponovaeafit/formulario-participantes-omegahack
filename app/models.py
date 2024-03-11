# from app import db

# class Equipo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(128), unique=True, index=True)
#     participantes = db.relationship('Participante', backref='equipo', lazy='dynamic')

#     def __repr__(self):
#         return '<Equipo {}>'.format(self.nombre)

# class Participante(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(128), index=True)
#     correo_institucional = db.Column(db.String(128), unique=True, index=True)
#     edad = db.Column(db.Integer)
#     universidad = db.Column(db.String(128))
#     carrera = db.Column(db.String(128))
#     sexo = db.Column(db.String(64))
#     participacion_hackathon = db.Column(db.Boolean, default=False)
#     tipo_inscripcion = db.Column(db.String(64))  # "equipo" or "individual"
#     rol = db.Column(db.String(128))
#     id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'))

#     def __repr__(self):
#         return '<Participante {}>'.format(self.nombre)