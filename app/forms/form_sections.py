from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Optional


class MainPageForm(FlaskForm):
    submit = SubmitField('Start')


class RegistrationTypeForm(FlaskForm):
    registration_type = RadioField('Register as', choices=[('individual', 'Individual'), ('group', 'Group')], validators=[DataRequired()])
    submit = SubmitField('Continue')


class UserDetailsForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo_institucional = StringField('Correo Institucional', validators=[DataRequired(), Email()])
    edad = IntegerField('Edad', validators=[DataRequired()])
    universidad = SelectField('Universidad', choices=[
        ('', 'Seleccione una'),
        ('uni1', 'Universidad 1'),
        ('uni2', 'Universidad 2'),
        # Add other universities here
    ], validators=[DataRequired()])
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


class RoleSelectionForm(FlaskForm):
    role = RadioField('Select Your Role', choices=[
        ('role1', 'Role 1'),
        ('role2', 'Role 2'),
        ('role3', 'Role 3'),
        ('role4', 'Role 4')
    ], validators=[DataRequired()])
    submit = SubmitField('Continue')


class JoinTeamForm(FlaskForm):
    existing_team = SelectField('Join an Existing Team', coerce=int, validators=[Optional()])
    new_team_name = StringField('Or Create a New Team', validators=[Optional()])
    submit = SubmitField('Submit')