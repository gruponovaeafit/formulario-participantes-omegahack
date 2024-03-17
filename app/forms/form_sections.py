from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Optional
from app.models import Universidad, Role, Equipo


class MainPageForm(FlaskForm):
    submit = SubmitField('Start')


class RegistrationTypeForm(FlaskForm):
    registration_type = RadioField('Register as', choices=[('individual', 'Individual'), ('group', 'Group')], validators=[DataRequired()])
    submit = SubmitField('Continue')


class UserDetailsForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo_institucional = StringField('Correo Institucional', validators=[DataRequired(), Email()])
    edad = IntegerField('Edad', validators=[DataRequired()])
    universidad = SelectField('Universidad', coerce=int)  # Note the coerce=int for handling IDs
    carrera = StringField('Carrera', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[
        ('', 'Seleccione uno'),
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('no_decir', 'Prefiero no decir'),
    ], validators=[DataRequired()])
    participado_hackathon = BooleanField('He participado en otra hackathon')
    submit = SubmitField('Continuar')

    def __init__(self, *args, **kwargs):
        super(UserDetailsForm, self).__init__(*args, **kwargs)
        self.universidad.choices = [(0, 'Seleccione una')] + [(u.id, u.nombre) for u in Universidad.query.order_by('nombre')]


class RoleSelectionForm(FlaskForm):
    role = RadioField('Seleccione su rol', choices=[], validators=[DataRequired()])
    submit = SubmitField('Continue')


class JoinTeamForm(FlaskForm):
    existing_team = SelectField('Join an Existing Team', coerce=int, validators=[Optional()])
    new_team_name = StringField('Or Create a New Team', validators=[Optional()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(JoinTeamForm, self).__init__(*args, **kwargs)
        # Dynamically set choices for existing teams
        self.existing_team.choices = [(0, 'Select a Team')] + [(team.id, team.nombre) for team in Equipo.query.order_by('nombre').all()]