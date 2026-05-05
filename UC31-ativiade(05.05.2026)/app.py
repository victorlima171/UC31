from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    meu_nome = "Seu Nome Aqui"  # Substitua pelo seu nome real, se desejar
    return render_template("login.html", nome=meu_nome)

if __name__ == "__main__":
    app.run(debug=True)