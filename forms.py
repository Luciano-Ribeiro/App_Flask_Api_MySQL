from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, EmailField, SelectField
from wtforms.validators import DataRequired, Length





class EditarForm(FlaskForm):
    list_estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PE",
                    "PI",
                    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    nome = StringField("nome", validators=[DataRequired()])
    pais = StringField("pais", validators=[DataRequired()])
    estado = SelectField("estado", validators=[DataRequired()], choices=list_estados)
    municipio = StringField("municipio", validators=[DataRequired()])
    cep = IntegerField("cep", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = IntegerField("numero", validators=[DataRequired()])
    complemento = StringField("complemento")
    cpf = StringField("cpf", validators=[DataRequired(),Length(max=11)])
    pis = StringField("pis", validators=[DataRequired(),Length(max=11)])

class CadastroForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("nome", validators=[DataRequired()])
    pais = StringField("pais", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])
    municipio = StringField("municipio", validators=[DataRequired()])
    cep = IntegerField("cep", validators=[DataRequired()])
    rua = StringField("rua", validators=[DataRequired()])
    numero = IntegerField("numero", validators=[DataRequired()])
    complemento = StringField("complemento")
    cpf = IntegerField("cpf", validators=[DataRequired()])
    pis = IntegerField("pis", validators=[DataRequired()])
    senha = PasswordField("pis", validators=[DataRequired()])

