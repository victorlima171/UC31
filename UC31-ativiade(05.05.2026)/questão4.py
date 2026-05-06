from flask import Flask, render_template

app = Flask(__name__)

@app.route("/arearestrita/<int:id>")
def area_restrita(id):
    if id == 1:
        imagem = "cadeado_fechado.png"
        mensagem = "Acesso Restrito"
    elif id == 2:
        imagem = "cadeado_aberto.png"
        mensagem = "Acesso Liberado"
    else:
        imagem = None
        mensagem = "ID inválido"
    return render_template("arearestrita.html", imagem=imagem, mensagem=mensagem)

@app.route("/operacao/<tipo>/<int:op1>/<int:op2>")
def operacao(tipo, op1, op2):
    if tipo == "sum":
        resultado = op1 + op2
        operacao_nome = "Soma"
    elif tipo == "sub":
        resultado = op1 - op2
        operacao_nome = "Subtração"
    elif tipo == "mult":
        resultado = op1 * op2
        operacao_nome = "Multiplicação"
    elif tipo == "div":
        if op2 == 0:
            return "Erro: Divisão por zero não permitida."
        resultado = op1 / op2
        operacao_nome = "Divisão"
    else:
        return "Tipo de operação inválido."
    return f"{operacao_nome} entre {op1} e {op2} = {resultado}"

if __name__ == "__main__":
    app.run(debug=True)