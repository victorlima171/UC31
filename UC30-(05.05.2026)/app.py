from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome = 'Victor'
    return render_template('index.html', title='Página de Contato', nome=nome)

@app.route('/usuario')
def usuario():
    usuario = {'nome': 'Victor', 'email': 'victor@example.com'}
    return render_template('index.html', title='Página do Usuário', usuario=usuario)

if __name__ == '__main__':
    app.run()