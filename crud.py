from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = sqlalchemy(app)


class Pessoa(db.Model):

    __tablename__ = "cliente"

    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String)
    razao_social = db.Column(db.String)
    cnpj = db.Column(db.String)
    data_inclusao = db.Column(db.Integer)

    def __init__(self,nome,razao_social,cnpj,data_inclusao):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao


db.create_all()


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        razao_social = request.form.get("razao_social")
        cnpj = request.form.get("cnpj")
        data_inclusao = request.form.get("data_inclusao")
    
        if nome and razao_social and cnpj and data_inclusao:
            p = Pessoa(nome, razao_social, cnpj, data_inclusao)
            db.session(p)
            db.session.commit()

    return redirect(url_for("index"))

@app.route("/lista")
def lista():
    pessoas = Pessoa.query.all()
    return render_template("lista.html",pessoas=pessoas)

@app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template("lista.html",pessoas=pessoas)

@app.route("/atualizar/<int:id>, methods=['GET' , 'POST']")
def atualizar(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        razao_social = request.form.get("razao_social")
        data_inclusao = request.form.get("data_inclusao")
    
        if nome and razao_social and data_inclusao:
            pessoa.nome = nome
            pessoa.razao_social = razao_social
            pessoa.data_inclusao = data_inclusao


            db.session.commit()

            return redirect(url_for("lista"))

    return render_template("atualizar.html", pessoa=pessoa)



if __name__ == "__main__":
    app.run(debug=True)

