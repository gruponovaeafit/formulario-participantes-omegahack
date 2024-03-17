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
    if form.validate_on_submit():
        # Example of creating a new participant record with the registration type
        # You might need to adjust this based on whether you're creating a new participant
        # Or updating an existing one (e.g., based on session data or a logged-in user)
        new_participant = Participante(tipo_inscripcion=form.registration_type.data)
        db.session.add(new_participant)
        db.session.commit()

        # Assuming you want to track the participant's ID in the session to update the same record later
        session['participant_id'] = new_participant.id

        return redirect(url_for('user_details'))

    return render_template('register.html', form=form, show_progress=True, progress_percentage=25)


@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    form = UserDetailsForm()

    # Attempt to retrieve the existing participant ID from the session
    participant_id = session.get('participant_id')

    # If there's no participant ID in the session, redirect to the start of the registration process
    # This is a safety check and depends on your application's flow
    if not participant_id:
        return redirect(url_for('register'))  # Adjust to your initial form step

    if form.validate_on_submit():
        # Fetch the participant record from the database
        participant = Participante.query.get(participant_id)

        # Update the participant record with details from the form
        participant.nombre = form.nombre.data
        participant.correo_institucional = form.correo_institucional.data
        participant.edad = form.edad.data
        # Assuming universidad field is a SelectField returning the ID of the Universidad
        selected_universidad = Universidad.query.get(form.universidad.data)
        participant.universidad = selected_universidad  # Assuming 'universidad' is a relationship field
        participant.carrera = form.carrera.data
        participant.sexo = form.sexo.data
        participant.participacion_hackathon = form.participado_hackathon.data

        # Save the updated record to the database
        db.session.commit()

        return redirect(url_for('role_selection'))  # Adjust to your next form section

    return render_template('user_details.html', form=form, show_progress=True, progress_percentage=55)


@app.route('/role_selection', methods=['GET', 'POST'])
def role_selection():
    form = RoleSelectionForm()

    participant_id = session.get('participant_id')
    if not participant_id:
        # Redirect to the start if no participant ID is found in session
        return redirect(url_for('register'))

    participant = Participante.query.get(participant_id)
    if participant is None:
        flash('Participant not found. Please start the registration process again.', 'error')
        return redirect(url_for('register'))  # Adjust as needed

    if form.validate_on_submit():
        # Update the participant's role based on the form data
        selected_role = Role.query.get(form.role.data)
        participant.rol = selected_role  # Assuming 'rol' is a relationship field
        db.session.commit()

        if participant.tipo_inscripcion == 'group':
            return redirect(url_for('team_selection'))
        else:
            return redirect(url_for('final_submit'))

    return render_template('role_selection.html', form=form, show_progress=True, progress_percentage=75)


@app.route('/team_selection', methods=['GET', 'POST'])
def team_selection():
    form = JoinTeamForm()
    # Dynamically set choices for existing teams
    form.existing_team.choices = [(0, 'Select a Team')] + [(team.id, team.name) for team in Equipo.query.order_by(Equipo.nombre).all()]

    participant_id = session.get('participant_id')
    if not participant_id:
        flash('Your session has expired, please start again.', 'warning')
        return redirect(url_for('register'))

    if form.validate_on_submit():
        participant = Participante.query.get(participant_id)

        if form.new_team_name.data:  # User wants to create a new team
            new_team = Equipo(nombre=form.new_team_name.data)
            db.session.add(new_team)
            db.session.flush()  # Flush to get the new team ID before commit if needed

            # Link the participant with the newly created team
            participant.id_equipo = new_team.id

        elif form.existing_team.data and form.existing_team.data != 0:  # User wants to join an existing team
            # Update participant's team ID to the selected existing team
            participant.id_equipo = form.existing_team.data

        db.session.commit()

        return redirect(url_for('final_submit'))

    return render_template('team_selection.html', form=form)


@app.route('/final_submit', methods=['GET', 'POST'])
def final_submit():
    participant_id = session.get('participant_id')
    if not participant_id:
        # If there's no ongoing registration process, redirect to start
        flash('Your session has expired, please start the registration process again.', 'warning')
        return redirect(url_for('register'))

    participant = Participante.query.get(participant_id)
    if not participant:
        flash('An unexpected error occurred. Please try registering again.', 'error')
        return redirect(url_for('register'))

    # Perform any final actions needed for the participant's registration
    # This could include setting a registration complete flag, sending an email, etc.

    db.session.commit()

    # Clear the participant ID from the session to clean up
    session.pop('participant_id', None)

    # Redirect to a confirmation page, dashboard, or another appropriate location
    return render_template('registration_confirmation.html', participant=participant)