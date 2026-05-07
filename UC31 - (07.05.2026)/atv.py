from flask import Flask, render_template

app = Flask(__name__)

sabores = {
    "frango": {
        "nome": "Frango",
        "imagem": "frango.jpg"
    },
    "portuguesa": {
        "nome": "Portuguesa",
        "imagem": "portuguesa.jpg"
    },
    "queijo": {
        "nome": "Queijo",
        "imagem": "queijo.jpg"
    }
}

@app.route('/pizzaria/<sabor>')
def pizza(sabor):
    info = sabores.get(sabor)
    if info:
        return render_template('pizza.html', nome=info["nome"], imagem=info["imagem"])
    else:
        return render_template('pizza.html', nome="este sabor não está disponível", imagem=None)

if __name__ == '__main__':
    app.run(debug=True)