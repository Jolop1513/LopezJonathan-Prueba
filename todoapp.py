from flask import Flask, render_template, request, redirect, url_for, flash, json
from os.path import exists, os

app = Flask(__name__, template_folder='templates')

app.secret_key = 'mysecretkey'

# Array for save tasks
tasks = []

"""
Representa la plantilla index.html, pasando la variable de tareas
:return: Se está devolviendo el archivo index.html.
"""

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)




# Running the app.
if __name__ == '__main__':
    app.run(debug=True)
