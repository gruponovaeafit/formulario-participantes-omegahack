from flask import render_template, redirect, url_for, session
from app import app
# from app.models import Team
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
        # Store the choice in session or database as needed
        session['registration_type'] = form.registration_type.data
        
        return redirect(url_for('user_details'))

    return render_template('register.html', form=form, show_progress=True, progress_percentage=25)


@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    form = UserDetailsForm()
    if form.validate_on_submit():
        # Store form data in session or database
        session['user_details'] = {
            'nombre': form.nombre.data,
            'correo_institucional': form.correo_institucional.data,
            'edad': form.edad.data,
            'universidad': form.universidad.data,
            'carrera': form.carrera.data,
            'sexo': form.sexo.data,
            'participado_hackathon': form.participado_hackathon.data
        }
        return redirect(url_for('role_selection'))  # Adjust to your next form section

    return render_template('user_details.html', form=form, show_progress=True, progress_percentage=55)


@app.route('/role_selection', methods=['GET', 'POST'])
def role_selection():
    form = RoleSelectionForm()
    if form.validate_on_submit():
        # Save the selected role in the session or database
        session['selected_role'] = form.role.data
        return redirect(url_for('team_selection'))  # Replace 'next_section' with your actual next section

    return render_template('role_selection.html', form=form, show_progress=True, progress_percentage=75)


@app.route('/team_selection', methods=['GET', 'POST'])
def team_selection():
    form = JoinTeamForm()
    form.existing_team.choices = [(0, 'Select a Team')] + [(team.id, team.name) for team in Team.query.order_by(Team.name).all()]

    # if form.validate_on_submit():
    #     if form.new_team_name.data:  # User wants to create a new team
    #         new_team = Team(name=form.new_team_name.data)
    #         db.session.add(new_team)
    #         db.session.commit()
    #         # Register the user in the new team
    #         # You'll need to add logic here to link the user with the newly created team
    #     elif form.existing_team.data != 0:  # User wants to join an existing team
    #         # Logic to register the user in the selected team
    #         # This also requires updating user's data to reflect team membership
    #     return redirect(url_for('final_submit'))  # Adjust to your actual final submission route

    return render_template('team_selection.html', form=form)