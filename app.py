from flask import Flask, request, render_template
import random

app = Flask(__name__)

jugadas = ["piedra", "papel", "tijera"]

def determinar_ganador(jugador, servidor):
    if jugador == servidor:
        return "Empate"
    elif (jugador == "piedra" and servidor == "tijera") or \
         (jugador == "papel" and servidor == "piedra") or \
         (jugador == "tijera" and servidor == "papel"):
        return "Jugador"
    else:
        return "Servidor"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/jugar', methods=['POST'])
def jugar():
    jugador = request.form.get("jugada")
    if jugador not in jugadas:
        return render_template("index.html", resultado="Jugada inválida", jugador="Desconocido", servidor="Desconocido")

    servidor = random.choice(jugadas)
    resultado = determinar_ganador(jugador, servidor)

    return render_template("index.html", jugador=jugador, servidor=servidor, resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
