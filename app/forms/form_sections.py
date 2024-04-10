from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email, Optional
from app.models import Universidad, Role, Equipo
from wtforms.validators import NumberRange
from app.models import Participante


class MainPageForm(FlaskForm):
    tratamiento_datos = BooleanField('He leido y acepto los términos y condiciones', validators=[
        DataRequired(message="Debe aceptar la política de tratamiento de datos para proceder.")
    ])
    submit = SubmitField('Continuar')


class TeamSelectionForm(FlaskForm):
    equipo = SelectField('Equipo', coerce=int, validators=[DataRequired(message="Seleccione un equipo")])
    submit = SubmitField('Continuar')

    def __init__(self, *args, **kwargs):
        super(TeamSelectionForm, self).__init__(*args, **kwargs)
        self.equipo.choices = [(0, 'Seleccione un equipo')] + [
            (equipo.id, equipo.nombre) for equipo in Equipo.query.order_by(Equipo.nombre).all()
        ]


class PersonalInformationForm(FlaskForm):
    # Assuming the 'nombre' field will be filled based on the previous selection
    nombre = SelectField('Nombre Completo', coerce=int, validators=[DataRequired()])
    semestre = IntegerField('Semestre', validators=[DataRequired(), NumberRange(min=1, max=10, message="El semestre debe estar entre 1 y 10.")])
    eps = StringField('EPS', validators=[DataRequired()])
    contacto_emergencia = StringField('Número de Celular', validators=[DataRequired()])
    parentesco_contacto_emergencia = StringField('Parentesco', validators=[DataRequired()])
    alergias = StringField('Alergias', validators=[DataRequired()])
    enfermedades = StringField('Enfermedades', validators=[DataRequired()])
    numero_contacto_emergencia = StringField('Número de contacto de emergencia', validators=[DataRequired()])
    seguridad_asistencia = BooleanField('He leído y acepto los términos y condiciones', validators=[DataRequired(message="Debe aceptar la política de tratamiento de datos para proceder.")])
    submit = SubmitField('Enviar')

    def validate_semestre(self, field):
        if field.data < 1 or field.data > 10:
            raise ValidationError("El semestre debe estar entre 1 y 10.")
