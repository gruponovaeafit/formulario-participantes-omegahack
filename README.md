# Formulario de inscripción. OmegaHack
## Equipo
* Zcharick Romero: Diseñadora
* Stiven Gómez: Diseñador
* Julián Agudelo: Desarrollador
* Katherin Allín: Analísta
* Kevin Quiroz: Desarrollador
* Alejandro Ríos: Desarrollador
* Manuela Caro: Líder de Proyecto


## Problemática

En el semestre 2024-1 se desarrollará el evento La OmegaHack, creado por el grupo estudiantil Nova. Para este evento, en aspectos logísticos, se necesitaba almacenar la información de los participantes para la creación de equipos, distribución de información y se almacena los datos para posuble estudio para futuras Omegahack´s.

## Solución

Se decidió crear un formulario, propio del grupo estudiantil Nova, para el almacenamiento de datos de los participantes en el evento OmegaHack. Donde, por decisión propia del equipo, se hizo el formulario desde cero. Utilizando Figma para la creación del diseño, Flask y FlaskWTF para el backend, HTML y CSS (sin ninguna librería) para el frontend y Azure para la base de datos.

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
