#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
#	return render_template('index.html')

###

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    mensagem = ''
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = f"Obrigado, {nome}! Recebemos seu e-mail: {email}."
    return render_template('index2.html', titulo='Formulário de Contato', mensagem=mensagem)

