from flask import flash, render_template, redirect, url_for, session
from app import app, db
from app.models import Equipo, Participante, Role, Universidad
from app.forms.form_sections import MainPageForm, RegistrationTypeForm, UserDetailsForm, RoleSelectionForm, JoinTeamForm

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = MainPageForm()
    if form.validate_on_submit():
        return redirect(url_for('register'))
    return render_template('main_page.html', form=form, show_progress=True, progress_percentage=0)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationTypeForm()
    # Create a variable that will allow to control only user that started from the main page can access the registration
    session['started_registration'] = True
    if form.validate_on_submit():
        # Store the registration type in the session
        session['registration_type'] = form.registration_type.data
        # Redirect to the next form step
        return redirect(url_for('user_details'))

    return render_template('register.html', form=form, show_progress=True, progress_percentage=25)


@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    # Is the user allowed to access this page?
    if not session.get('started_registration'):
        flash('Please start the registration process from the main page.', 'warning')
        return redirect(url_for('main_page'))

    form = UserDetailsForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Accumulate user details in the session
        session['user_details'] = {
            'nombre': form.nombre.data,
            'correo_institucional': form.correo_institucional.data,
            'edad': form.edad.data,
            'universidad': form.universidad.data,
            'carrera': form.carrera.data,
            'sexo': form.sexo.data,
            'participado_hackathon': form.participado_hackathon.data
        }
        print(session['user_details'])
        return redirect(url_for('role_selection'))

    return render_template('user_details.html', form=form, show_progress=True, progress_percentage=55)


@app.route('/role_selection', methods=['GET', 'POST'])
def role_selection():
    if not session.get('started_registration'):
        flash('Please start the registration process from the main page.', 'warning')
        return redirect(url_for('main_page'))
    
    form = RoleSelectionForm()
    form.role.choices = [(role.id, role.nombre) for role in Role.query.order_by(Role.nombre).all()]

    if form.validate_on_submit():
        # Store the selected role in the session
        session['selected_role_id'] = form.role.data
        
        # Determine the next step based on the participant's registration type
        registration_type = session.get('registration_type')
        if registration_type == 'group':
            return redirect(url_for('team_selection'))
        else:
            # For individual registrations, proceed to finalization or another appropriate step
            return redirect(url_for('final_submit'))

    return render_template('role_selection.html', form=form, show_progress=True, progress_percentage=75)


@app.route('/team_selection', methods=['GET', 'POST'])
def team_selection():
    if not session.get('started_registration'):
        flash('Please start the registration process from the main page.', 'warning')
        return redirect(url_for('main_page'))
    
    form = JoinTeamForm()
    form.existing_team.choices = [(0, 'Select a Team')] + [(team.id, team.nombre) for team in Equipo.query.order_by(Equipo.nombre).all()]

    if form.validate_on_submit():
        if form.new_team_name.data:  # User wants to create a new team
            new_team = Equipo(nombre=form.new_team_name.data)
            db.session.add(new_team)
            db.session.commit()
            # Update the session with the newly created team's ID
            session['team_id'] = new_team.id
        elif form.existing_team.data and form.existing_team.data != 0:  # User wants to join an existing team
            # Update the session with the selected existing team's ID
            session['team_id'] = form.existing_team.data

        
        return redirect(url_for('final_submit'))

    return render_template('team_selection.html', form=form)


@app.route('/final_submit', methods=['GET'])
def final_submit():
    if not session.get('started_registration'):
        flash('Please start the registration process from the main page.', 'warning')
        return redirect(url_for('main_page'))
    # Assuming all necessary data is stored in the session
    user_details = session.get('user_details')
    selected_role_id = session.get('selected_role_id')
    team_id = session.get('team_id')

    # Check if we have the minimum required data to create a participant
    if user_details:
        # Create a new participant instance
        new_participant = Participante(
            nombre=user_details.get('nombre'),
            correo_institucional=user_details.get('correo_institucional'),
            edad=user_details.get('edad'),
            universidad_id=user_details.get('universidad'),  # Ensure this is the ID, not the name
            carrera=user_details.get('carrera'),
            sexo=user_details.get('sexo'),
            participacion_hackathon=user_details.get('participado_hackathon', False),
            tipo_inscripcion=session.get('registration_type', 'individual'),  # Default to 'individual'
            rol_id=selected_role_id,
            id_equipo=team_id  # This can be None if no team was selected
        )
        db.session.add(new_participant)
        print(new_participant)
        db.session.commit()
        

        # Clear the session data now that we've successfully registered the participant
        session.pop('user_details', None)
        session.pop('selected_role_id', None)
        session.pop('team_id', None)
        session.pop('registration_type', None)

        # Redirect to a confirmation page with the new participant's details
        return render_template('registration_confirmation.html', participant=new_participant)
    else:
        # If required details are missing, redirect to the start or an error handling page
        flash('Registration details missing. Please start the registration process again.', 'warning')
        return redirect(url_for('register'))
