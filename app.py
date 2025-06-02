# Formulario con validación en cliente y servidor + feedback de errores 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "").strip()
    correo = request.form.get("correo", "").strip()

    if not nombre or not edad or not correo:
        return "Todos los campos son obligatorio."
    
    return f"Hola {nombre}, tienes {edad} años y tu correo es {correo}."


if __name__ == '__main__':
    app.run(debug=True)
