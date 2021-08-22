from config import *
from modelo import Pessoa

@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_pessoas")
def listar_pessoas():
    Pessoas = db.session.query(Pessoa).all()
    retorno = []
    for i in Pessoas:
        retorno.append(i.json())

    resposta = jsonify(retorno)
    return resposta

app.run(debug=True)