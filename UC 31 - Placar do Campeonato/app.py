from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "123"

@app.route('/')
def inicio():

    if 'brasil' not in session:
        session['brasil'] = 0
        session['argentina'] = 0
        session['franca'] = 0
        session['espanha'] = 0

    return render_template(
        'inicio.html',
        brasil=session['brasil'],
        argentina=session['argentina'],
        franca=session['franca'],
        espanha=session['espanha']
    )

@app.route('/ponto/<time>')
def ponto(time):

    session[time] += 1

    return redirect('/')

@app.route('/zerar')
def zerar():

    session['brasil'] = 0
    session['argentina'] = 0
    session['franca'] = 0
    session['espanha'] = 0

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)