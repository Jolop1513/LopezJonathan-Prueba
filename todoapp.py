from flask import Flask, render_template, request, redirect, url_for, flash, json
from os.path import exists, os

app = Flask(__name__, template_folder='templates')

app.secret_key = 'mysecretkey'

# Array para guardar a los clientes
registro = []

"""
Representa la plantilla index.html, pasando la variable de tareas
:return: Se está devolviendo el archivo index.html.
"""

@app.route('/')
def index():
    return render_template('index.html', registro=registro)
"""
    Si el método de solicitud es POST, obtenga registro_name, registro_telefono y registro_estado del cliente,
    y si alguno de ellos está vacío, muestra un mensaje de error y redirige a la página de índice, de lo contrario
    mostrar un mensaje de éxito y redirigir a la página de índice
    :return: el archivo index.html.
"""

@app.route('/enviar', methods=['POST'])
def enviar():
    # El método de solicitud de verificación es POST
    if request.method == 'POST':
        registro_name = request.form['registro_name']
        registro_telephone = request.form['registro_telephone']
        registro_priority = request.form['registro_priority']
        if registro_name == '' or registro_telephone == '':
            # Mensaje de error
            flash('Por favor ingrese todos los campos', 'peligro')
            # Redirigir a la página de índice
            return redirect(url_for('index'))
        else:
      
            registro_id = len(registro) + 1

            registro.append({'registro_id': registro_id, 'registro_name': registro_name,
                         'registro_telephone': registro_telephone, 'registro_priority': registro_priority})
            # Mensaje de éxito de Flask
            flash('Nuevo cliente agregado', 'éxito')
            # Redirigir a la página de índice
            return redirect(url_for('index'))
    else:
        # Return 404 error
        return 'Error 404'





# Running the app.
if __name__ == '__main__':
    app.run(debug=True)
