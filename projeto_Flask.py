from flask import Flask

#_name_ == _main_ quando executado de forma manual
app = Flask(__name__) 

#rota para comunicar com outros clientes ou usuarios
@app.route("/") # rota padrão usa /
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)