from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Login
@app.route('/login')
def login():
    return render_template('login.html')

# Cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Perfil
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

# Anúncios
@app.route('/anuncios')
def anuncios():
    return render_template('anuncios.html')

# Detalhe do anúncio
@app.route('/anuncio/<int:id>')
def detalhe_anuncio(id):
    return render_template('detalhe_anuncio.html', id=id)

if __name__ == "__main__":
    app.run(debug=True)