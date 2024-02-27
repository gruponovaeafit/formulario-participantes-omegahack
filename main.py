from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template('inicio.html')


@app.route('/nova')
def nova():
    return render_template('nova.html')

# prueba

if __name__ == "__main__":
    app.run(debug=True)
