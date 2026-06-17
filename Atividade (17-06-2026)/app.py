from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "123"

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    mensagem = ""

    if request.method == 'POST':

        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario == "Mariah" and senha == "123":

            session['usuario'] = usuario

            return redirect('/dashboard')

        else:
            mensagem = "Login inválido!"

    return render_template('login.html', mensagem=mensagem)


@app.route('/dashboard')
def dashboard():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        usuario=session['usuario']
    )


@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


@app.route('/rotalogin')
def rotalogin():
    return "Rota criada pela IA"


if __name__ == '__main__':
    app.run(debug=True)