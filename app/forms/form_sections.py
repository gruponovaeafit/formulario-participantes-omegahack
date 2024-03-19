from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email, Optional
from app.models import Universidad, Role, Equipo
from wtforms.validators import NumberRange
from app.models import Participante


class MainPageForm(FlaskForm):
    submit = SubmitField('Iniciar')


class RegistrationTypeForm(FlaskForm):
    registration_type = RadioField('Register as', choices=[('individual', 'Individual'), ('group', 'Group')], validators=[DataRequired()])
    submit = SubmitField('Continue')


class UserDetailsForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired()])
    correo_institucional = StringField('Correo Institucional', validators=[DataRequired(), Email()])
    edad = IntegerField('Edad', validators=[DataRequired(), NumberRange(min=10, max=80, message="La edad debe estar entre 10 y 80 años.")])
    universidad = SelectField('Universidad', coerce=int)  # Note the coerce=int for handling IDs
    carrera = StringField('Carrera', validators=[DataRequired()])
    sexo = SelectField('Genero', choices=[
        ('', 'Seleccione uno'),
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('no_decir', 'Prefiero no decir'),
    ], validators=[DataRequired()])
    participado_hackathon = BooleanField('He participado en otra hackathon')
    submit = SubmitField('Continuar')

    def validate_edad(self, field):  # Rename "form" to "self" or add the missing "self" parameter
        if field.data < 10 or field.data > 80:
            raise ValidationError("La edad debe estar entre 10 y 80 años.")

    def validate_correo_institucional(self, field):
        if Participante.query.filter_by(correo_institucional=field.data).first():
            raise ValidationError('Este correo ya está registrado. Por favor, usa otro.')

    def __init__(self, *args, **kwargs):
        super(UserDetailsForm, self).__init__(*args, **kwargs)
        self.universidad.choices = [(0, 'Seleccione una')] + [(u.id, u.nombre) for u in Universidad.query.order_by('nombre')]


class RoleSelectionForm(FlaskForm):
    role = RadioField('Seleccione su rol', choices=[], validators=[DataRequired()])
    submit = SubmitField('Continuar')


class JoinTeamForm(FlaskForm):
    existing_team = SelectField('Selecciona tu equipo', coerce=int, validators=[Optional()])
    new_team_name = StringField('Vamos a crear tu equipo', validators=[Optional()])
    submit = SubmitField('Enviar')

    def __init__(self, *args, **kwargs):
        super(JoinTeamForm, self).__init__(*args, **kwargs)
        # Dynamically set choices for existing teams
        self.existing_team.choices = [(0, 'Seleccionar un equipo')] + [(team.id, team.nombre) for team in Equipo.query.order_by('nombre').all()]