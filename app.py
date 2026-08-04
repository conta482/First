from flask import Flask , render_template

app = Flask (__nome__)

@app.route("/")
def home():
    dados = {
          "titulo": "Minha aplicação Flask", 
          "descrição": "Ambiente de desenvolvimento rodando localmente ."
    }

    return render_template ("index.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
