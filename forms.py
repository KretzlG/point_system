from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Formulário de login do sistema
class LoginForm(FlaskForm):
    # Campo para o nome de usuário (obrigatório)
    username = StringField('Usuário', validators=[DataRequired()])
    # Campo para a senha (obrigatório)
    password = PasswordField('Senha', validators=[DataRequired()])
    # Botão de envio do formulário
    submit = SubmitField('Entrar')