# uhttp/server.py
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
import os
import sys

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))


UPLOAD_FOLDER = 'uploads'  # Define la carpeta donde se guardarán los archivos subidos

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configura la carpeta de subidas en la aplicación Flask

# Crea la carpeta de subidas si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = []  # Lista para almacenar los resultados de los archivos subidos
        files = request.files.getlist('file')  # Obtiene la lista de archivos de la solicitud
        for file in files:
            file_result = {'filename': file.filename, 'success': False}  # Inicializa el resultado del archivo
            # Verifica si el archivo tiene un nombre (asegura que no está vacío)
            if file.filename == '':
                uploaded_files.append(file_result)
                continue  # Si el archivo no tiene nombre, pasa al siguiente archivo
            if file:  # Si hay un archivo válido
                filename = file.filename  # Obtiene el nombre del archivo
                try:
                    # Guarda el archivo en la carpeta de subidas
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    file_result['success'] = True  # Marca el archivo como subido con éxito
                except Exception as e:
                    file_result['success'] = False  # Marca el archivo como subido con error
            uploaded_files.append(file_result)  # Agrega el resultado del archivo a la lista
        return jsonify({'uploaded_files': uploaded_files})  # Devuelve el resultado en formato JSON
    # Renderiza la página principal si el método es GET
    return render_template('index.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     # Envía el archivo solicitado desde la carpeta de subidas
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def run():
    # Permite especificar el puerto desde la línea de comandos
    port = 5033  # Puerto predeterminado
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    run()
