from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    pagina = request.args.get('pagina', default=1, type=int)
    api = requests.get(f'https://rickandmortyapi.com/api/character?page={pagina}')
    personagens = api.json()
    return render_template("home.html", personagem=personagens['results'], pagina_atual=pagina)

@app.route("/personagem/<personagem>")
def enviar(personagem):
    api = requests.get(f'https://rickandmortyapi.com/api/character/{personagem}')
    personagem_id = api.json()
    return render_template("info.html", personagem_id = personagem_id)


if __name__ == "__main__":
    app.run()