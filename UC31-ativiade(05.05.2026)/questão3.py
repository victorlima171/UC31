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

if __name__ == "__main__":
    app.run(debug=True)