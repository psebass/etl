import chardet
import os
import pandas as pd
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify
from etl import limpiar_datos
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def allowed_file(filename):
    return ('.' in filename and filename.rsplit('.', 1)[1].lower()
             in ALLOWED_EXTENSIONS)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No se envió ningún archivo', 400

    archivos = request.files.getlist('file')
    procesados = []

    for file in archivos:
        if file.filename == '':
            continue 

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            with open(filepath, 'rb') as f:
                result = chardet.detect(f.read())
            encoding_detectado = result['encoding']

            if filename.endswith('.csv'):
                df = pd.read_csv(filepath, encoding=encoding_detectado)
            else:
                df = pd.read_excel(filepath, engine='openpyxl')

            df_clean = limpiar_datos(df)
            processed_filename = f"""procesado_{filename.replace('.xlsx',
                                                               '.csv')}"""
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], 
                                          processed_filename)
            df_clean.to_csv(processed_path, index=False)
            procesados.append(processed_filename)

    if not procesados:
        return 'No se procesó ningún archivo válido', 400

    return redirect(url_for('success', filename=procesados))


@app.route('/download/<filename>')
def download_file(filename):
    return (send_from_directory(app.config['PROCESSED_FOLDER'],
                                 filename, as_attachment=True))


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/archivos_procesados')
def archivos_procesados():
    carpeta = os.path.join(os.getcwd(), 'processed')
    if not os.path.exists(carpeta):
        return jsonify(archivos=[])

    archivos = [f for f in os.listdir(carpeta) 
                if os.path.isfile(os.path.join(carpeta, f))]
    return jsonify(archivos=archivos)


if __name__ == '__main__':
    app.run(debug=True)
