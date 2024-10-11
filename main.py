from flask import Flask, request, redirect, render_template, flash, url_for, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para utilizar o flash

# Configurações de upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16MB

# Garantir que a pasta de uploads exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica se a extensão do arquivo é permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    """Filtro personalizado para formatar timestamps."""
    return datetime.fromtimestamp(value).strftime(format)

@app.route('/')
def upload_form():
    """Renderiza o formulário de upload e lista os arquivos enviados."""
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_details = []
    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path) / 1024  # Tamanho em KB
            upload_time = os.path.getctime(file_path)  # Timestamp
            file_details.append({
                'name': file,
                'size': f"{file_size:.2f}",
                'upload_time': upload_time
            })
    return render_template('upload.html', files=file_details)

@app.route('/upload', methods=['POST'])
def upload_files():
    """Lida com o upload dos arquivos."""
    if 'files[]' not in request.files:
        flash('Nenhum arquivo parte da requisição')
        return redirect(request.url)
    
    files = request.files.getlist('files[]')
    if not files:
        flash('Nenhum arquivo selecionado')
        return redirect(request.url)
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Evita sobrescrever arquivos existentes
            if os.path.exists(file_path):
                flash(f'Arquivo {filename} já existe.')
                continue
            file.save(file_path)
            flash(f'Arquivo {filename} enviado com sucesso')
        else:
            flash(f'Arquivo {file.filename} não permitido')
    
    return redirect(url_for('upload_form'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Rota para servir os arquivos enviados."""
    if allowed_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        abort(404)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Rota para deletar um arquivo enviado."""
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f'Arquivo {filename} deletado com sucesso')
    else:
        flash(f'Arquivo {filename} não encontrado')
    return redirect(url_for('upload_form'))

@app.route('/view/<filename>')
def view_file(filename):
    """Rota para visualizar um arquivo."""
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        flash(f'Arquivo {filename} não encontrado')
        return redirect(url_for('upload_form'))
    
    # Identificar o tipo de arquivo para renderização
    file_ext = filename.rsplit('.', 1)[1].lower()
    if file_ext in {'png', 'jpg', 'jpeg', 'gif'}:
        return render_template('view_image.html', filename=filename)
    elif file_ext == 'pdf':
        return render_template('view_pdf.html', filename=filename)
    else:
        flash(f'Visualização não suportada para o arquivo {filename}')
        return redirect(url_for('upload_form'))

if __name__ == "__main__":
    app.run(debug=True)
