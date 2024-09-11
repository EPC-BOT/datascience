from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do Rei Barbearia"


@app.route('/novofuncionario')
def novoFuncionario():
    return "cadatrar novo funcionario"

@app.route('/novocliente')
def novoCliente():
    return "novo cliente cadastrado"

@app.route('/novoserviço')
def novoServico():
     return "novo servico"

@app.route('/novoagendamento')
def novoAgendamento():
        return "novo agendamento"

@app.route('/novologin')
def novoLogin():
    return "novo login"


@app.route('/novologout')
def novoLogout():
    return "novo logout"


app.run(debug=True)