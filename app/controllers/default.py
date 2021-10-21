from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user

from app import app, db, login_manager

from app.models.forms import LoginForm
from app.models.tables import User



@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = (User.query.filter_by(username=form.username.data).first())
        if user and  user.password == form.password.data:
            login_user(user)
            flash("Logado!")
            return redirect(url_for("index"))
        else:
            flash("Login Inválido!")
    return render_template('login.html', form=form)




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# função para realização de CRUD
"""@app.route("/teste/<info>")
@app.route("/teste" , defaults={"info": None})
def teste(info):
    r = User('marcusf', '1234', "Marcus Franco", 
    "marcus-franco@live.com")

    db.session.add(r)
    db.session.commit()
    print(r)
    return "ok"""