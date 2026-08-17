from app import app, db
from flask import render_template, url_for, request
from app.models import Contato


@app.route('/')
def homepage():
    usuario = "Gabriel Souza"
    idade = 18
    
    # context para salvar as variaveis e poder lançar elas pro HTML
    context = {
        'usuario': usuario,
        'idade': idade
    }
    
    return render_template('index.html', context=context)

# FORMA RECOMENDADA
@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    context = {}
      
    if request.method == 'POST':
        
        # cada request.form pega os dados que o usuário colocou no input do HTML
        nome = request.form['nome'] # pega o nome
        email = request.form['email'] # pega o email
        assunto = request.form['assunto'] # pega o assunto
        mensagem = request.form['mensagem'] # pega a mensagem
        
        # criação de uma instancia de contato
        usuario = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        # adicionar a instancia no DB
        db.session.add(usuario)
        db.session.commit()

            
    return render_template('contato_old.html', context=context)






# FORMA NÃO RECOMENDADA (mas não quer dizer que seja inválida)
@app.route('/contato_old/', methods=['GET', 'POST'])
def contato_old():
    context = {}
    
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa') # pega os argumentos da URL
        print(f"GET: {pesquisa}") # printa a respota no terminal
        
        context.update({'pesquisa': pesquisa}) # atualiza para a pesquisa não aparecer na URL
        
    if request.method == 'POST':
        
        # cada request.form pega os dados que o usuário colocou no input do HTML
        nome = request.form['nome'] # pega o nome
        email = request.form['email'] # pega o email
        assunto = request.form['assunto'] # pega o assunto
        mensagem = request.form['mensagem'] # pega a mensagem
        
        # criação de uma instancia de contato
        user1 = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        # adicionar a instancia no DB
        db.session.add(user1)
        db.session.commit()

            
    return render_template('contato_old.html', context=context)
