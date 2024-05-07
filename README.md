<h1 align="center">Formulario Participantes OmegaHack 2024 <img src="https://i.imgur.com/VmDq6UM.png" width="60"/> </h1>

Bienvenido al repositorio del Formulario de Participantes de OmegaHack 2024. Este proyecto fue desarrollado por el Grupo Estudiantil NOVA, de la Universidad EAFIT, en el semestre 2024-1. En este repositorio encontrarás toda la información relacionada con el desarrollo del proyecto, desde la problemática hasta la solución propuesta por el equipo.

Este proyecto hace parte de la ejecución del proyecto "Formulario Inscripción OmegaHack 2024", el cual constó de dos (2) desarrollos: el formulario de inscripción y el formulario de participantes. Este repositorio corresponde al desarrollo del formulario de participantes. Para más información sobre el desarrollo del formulario de inscripción, puedes acceder al siguiente [repositorio](https://github.com/gruponovaeafit/hackaton-2024). Ambos repositorios contienen la misma información relacionada al desarrollo y ejecución del proyecto.

## Equipo

<img src="https://i.imgur.com/i6GvBGq.png"/>


## Problemática

Durante el primer semestre de 2024 se llevará a cabo el evento La OmegaHack, organizado por el Grupo Estudiantil NOVA. En lo que respecta a los aspectos logísticos, será necesario almacenar la información de los participantes con el fin de formar equipos, distribuir información y conservar los datos para estudios futuros que podrían mejorar las ediciones siguientes de La OmegaHack.

## Solución

Se decidió que el Grupo Estudiantil NOVA desarrollara un formulario personalizado para el almacenamiento de datos de los participantes. Este formulario fue diseñado desde cero mediante un análisis técnico exhaustivo. Se utilizó Figma para la creación del diseño, mientras que el backend fue desarrollado con Flask y Flask-WTF. Para el frontend, se optó por HTML y CSS puro, sin la inclusión de librerías adicionales. Finalmente, se eligió Azure SQL como la plataforma para la infraestructura de la base de datos.

## Desarrollo

Se tuvo la primera reunión con un representante de cada área del equipo, donde se definió los requerimientos del formulario y las fechas límites para la ejecución de este. Empezando por el equipo de diseño y el tiempo que ellos requerían para realizar los mockups de las distintas vistas y se le daba paso a el equipo de desarrollo cuando estos finalizaban. 

Durante este proceso, el equipo de diseño observó una mejor viabilidad en hacer dos formularios; ya que, se necesitaba recolectar mucha información del participante, causando que el usuario se podría cansar de completar todos los datos. Por ello, el primer formulario se hizo con los datos primarios de los participantes y el segundo formulario con datos específicos, siendo este segundo, llenado por los usuarios finales, aquellos que confirmen su participación en el evento. 

Las fechas límites para la entrega del primer formulario se atrasaron por falta de tiempo que tenía el equipo, pero se logró entregar y con suficiente tiempo de inscripción para los usuarios.

Se tuvo una segunda reunión para acordar el tiempo de realización del segundo formulario, contando este con menos tiempo para su realización. Se establecieron, al igual que el primero, fechas límites y requerimientos; además de resolver dudas por parte del equipo. 

Aunque se tuvo más dificultades de tiempo, el segundo formulario se logró terminar y ser diligenciado por más de 60 participantes, sin graves problemas. 

## Análisis

El resultado fue muy satisfactorio para el evento. Al utilizar Azure no se tuvo vulnerabilidad y el riesgo de exponer información privada de los participantes; tampoco hubo error en diligenciar el formulario, la información se procesaba exitosamente. 

### Aciertos

La idea de dividir el formulario en dos ha sido una buena estrategia. Ayudó a los organizadores de la OmegaHack a filtrar aquellas personas que ya no asistirían al evento y no fue tedisoso, para los participantes, llenar todos los datos que requeriamos para su participación. 

### Desaciertos

La ignorancia del equipo con respecto al manejo del tiempo retrasó la entrega de los formularios, afectó no hacer sprints durante el proceso y no contamos con el tiempo de aprender a manejar nuevas tecnologías.

### Soluciones

* Estar en constante seguimiento con el equipo y su progreso. 
* Calcular mejor los tiempos para la realización de las asignaciones y sumarle un tiempo extra en caso de existir contratiempos.

## Aprendizajes

* Conocimientos de buenas tecnologías.
* Importante manejo del tiempo.
* Crear un diseño a partir del usuario.
* Trabajo en equipo.

# OmegaHack 2024

## Install and execute

1. Clone the repository

```bash
git clone
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Activate the virtual environment (Linux and Windows)

- Linux

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

4. Install the requirements

```bash
pip install -r requirements.txt
```

5. Run the application

```bash
python3 run.py
```
