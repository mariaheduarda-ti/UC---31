from flask import Flask, session

app = Flask(__name__)

app.secret_key = "123"

@app.route('/contador')
def contador():

    visitas = session.get('visitas', 0)

    visitas += 1

    session['visitas'] = visitas

    return f'''
    <h1>Você acessou {visitas} vezes.</h1>
    <a href="/zerar">Zerar</a>
    '''

@app.route('/zerar')
def zerar():

    session.pop('visitas', None)

    return '''
    <h1>Contador zerado!</h1>
    <a href="/contador">Voltar</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)