from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    # Lista os projetos em HTML, CSS, Flask e Python
    return render_template("portfolio.html", projects=[
        {
            "title": "Projeto 1",
            "description": "Descrição do projeto 1",
            "image": "/static/img/projeto1.jpg"
        },
        {
            "title": "Projeto 2",
            "description": "Descrição do projeto 2",
            "image": "/static/img/projeto2.jpg"
        }
    ])

@app.route("/powerbi")
def powerbi():
    # Lista os relatórios e dashboards em Power BI
    return render_template("powerbi.html", reports=[
        {
            "title": "Relatório 1",
            "description": "Descrição do relatório 1",
            "image": "/static/img/relatorio1.jpg"
        },
        {
            "title": "Dashboard 1",
            "description": "Descrição do dashboard 1",
            "image": "/static/img/dashboard1.jpg"
        }
    ])

@app.route("/automation")
def automation():
    # Demonstração de serviços de automação e manipulação de dados em Python
    return render_template("automation.html")

@app.route("/contact")
def contact():
    # Informações de contato
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
