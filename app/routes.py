from flask import flash, render_template, redirect, request, url_for, session
from app import app, db
from app.models import Equipo, ParticipanteSeleccionado, Role, Universidad, Participante
from app.forms.form_sections import MainPageForm, TeamSelectionForm, PersonalInformationForm
from flask import jsonify

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = MainPageForm()
    if form.validate_on_submit():
        session['data_treatment_agreement'] = form.tratamiento_datos.data
        return redirect(url_for('select_team'))
    return render_template('main_page.html', form=form)


@app.route('/select_team', methods=['GET', 'POST'])
def select_team():
    form = TeamSelectionForm()
    form.equipo.choices = [(0, 'Seleccione un equipo')] + [
        (equipo.id, equipo.nombre) for equipo in Equipo.query.order_by('nombre').all()
    ]
    if form.validate_on_submit():
        session['equipo_id'] = form.equipo.data
        return redirect(url_for('personal_information', equipo_id=form.equipo.data))
    return render_template('select_team.html', form=form)


@app.route('/personal_information/<int:equipo_id>', methods=['GET', 'POST'])
def personal_information(equipo_id):
    form = PersonalInformationForm()
    form.nombre.choices = [(0, 'Seleccione su nombre')] + [
        (participante.id, participante.nombre) for participante in ParticipanteSeleccionado.query.filter_by(id_equipo=equipo_id).order_by(ParticipanteSeleccionado.nombre).all()
    ]

    if form.validate_on_submit():
        # Store all form data in session
        session['personal_information'] = {
            'nombre_id': form.nombre.data,
            'semestre': form.semestre.data,
            'eps': form.eps.data,
            'contacto_emergencia': form.contacto_emergencia.data,
            'parentesco_contacto_emergencia': form.parentesco_contacto_emergencia.data,
            'alergias': form.alergias.data,
            'enfermedades': form.enfermedades.data,
            'numero_contacto_emergencia': form.numero_contacto_emergencia.data,
            'seguridad_asistencia': form.seguridad_asistencia.data
        }
        return redirect(url_for('registration_confirmation'))

    return render_template('personal_information.html', form=form, equipo_id=equipo_id)


@app.route('/registration_confirmation', methods=['GET'])
def registration_confirmation():
    if 'personal_information' not in session or 'equipo_id' not in session:
        # Redirect if required data is missing
        return redirect(url_for('main_page'))

    equipo = Equipo.query.get(session['equipo_id'])
    personal_info = session['personal_information']
    # Assuming nombre_id is stored in personal_info and it's the ID of ParticipanteSeleccionado
    participante_seleccionado = ParticipanteSeleccionado.query.get(personal_info['nombre_id'])
    
    # Preparing data for the template
    data = {
        'equipo_nombre': equipo.nombre if equipo else 'N/A',
        'participante_nombre': participante_seleccionado.nombre if participante_seleccionado else 'N/A',
        'semestre': personal_info.get('semestre', 'N/A'),
        'eps': personal_info.get('eps', 'N/A'),
        'contacto_emergencia': personal_info.get('contacto_emergencia', 'N/A'),
        'parentesco_contacto_emergencia': personal_info.get('parentesco_contacto_emergencia', 'N/A'),
        'alergias': personal_info.get('alergias', 'N/A'),
        'enfermedades': personal_info.get('enfermedades', 'N/A'),
        'numero_contacto_emergencia': personal_info.get('numero_contacto_emergencia', 'N/A'),
        'seguridad_asistencia': 'Yes' if personal_info.get('seguridad_asistencia') else 'No'
    }

    return render_template('registration_confirmation.html', data=data)


@app.route('/finalize_registration', methods=['POST'])
def finalize_registration():
    personal_info = session.get('personal_information')

    if personal_info:
        participante = Participante(
            # Assuming 'nombre_id' refers to the ID of a selected participant, adjust accordingly
            id_participante_seleccionado=personal_info.get('nombre_id'),
            semestre=personal_info.get('semestre'),
            eps=personal_info.get('eps'),
            contacto_emergencia=personal_info.get('contacto_emergencia'),
            parentesco_contacto_emergencia=personal_info.get('parentesco_contacto_emergencia'),
            alergias=personal_info.get('alergias'),
            enfermedades=personal_info.get('enfermedades'),
            numero_contacto_emergencia=personal_info.get('numero_contacto_emergencia'),
            tratamiento_datos=session.get('data_treatment_agreement', False),
            seguridad_asistencia=personal_info.get('seguridad_asistencia', False)
        )
        db.session.add(participante)
        db.session.commit()

        # Clear session data after saving
        session.clear()

        return redirect(url_for('success_page'))
    
    # If the session data is missing, redirect to the start
    return redirect(url_for('main_page'))


@app.route('/success_page')
def success_page():
    return render_template('success.html')
