from app import app
from flask import render_template, url_for


@app.route('/')
def homepage():
    usuario = "Gabriel Souza"
    idade = 18
    
    context = {
        'usuario': usuario,
        'idade': idade
    }
    
    return render_template('index.html', context=context)

@app.route('/contatos/')
def novapag():
    return "Você está na página de contatos!"