# BIBLIOTECAS PARA CRIAR FORMULÁRIOS ORGANIZADOS E PROTEGIDOS
from flask_wtf import FlaskForm # para tratamento de formulários no Flask
from wtforms import EmailField, StringField, SubmitField # para informar o tipo que o campo da informação vai ter (é o type='...' no HTML)
from wtforms.validators import DataRequired, Email # verifica se as informações inseridas no campo está correta (nesse caso: se tem qualquer informação e se tem um email)

# classe que controla as informações do formulário
class ContatoForm(FlaskForm):
        nome = StringField("Nome", validators=[DataRequired()])
        email = EmailField("E-mail", validators=[DataRequired(), Email()])
        assunto = StringField("Assunto", validators=[DataRequired()])
        mensagem = StringField("Mensagem", validators=[DataRequired()])
        botaoSubmit = SubmitField("Enviar")