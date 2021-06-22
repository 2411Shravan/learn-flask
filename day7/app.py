from flask import Flask, redirect, url_for, render_template, request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="shravan_erefre"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
app.permanent_session_lifetime = timedelta(days=2)
db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    email= db.Column(db.String(50))

    def __init__(self, name,email):
        self.name=name
        self.email=email





a = False

names= ['shravan','shreyas','praveen','pradyumna','chandan','ashik']
er = 'right'


@app.route('/')
@app.route('/home')
def home():
    return render_template('./index.html',ere=er)


@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nam']
        session['user'] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email



        else:
            usr=users(user,"")
            db.session.add(usr)
            db.session.commit()


        flash(f'welcome to the application {user}','info')
        return redirect(url_for("user"))
    else:

        if "user" in session:
            user = session["user"]
            flash(f"Already logged in {user}",'info')
            return redirect(url_for("user"))
        return render_template('./login.html')

@app.route("/view/")
def view():
    return render_template('./view.html',values=users.query.all())



@app.route("/<error>")
def error(error):
    return render_template('./error.html',error=error)

@app.route("/user/", methods=["POST","GET"])
def user():
    email= None

    if "user" in session :
        user = session["user"]

        if request.method == 'POST':
            email= request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email=email
            db.session.commit()
            flash(f"Your email is saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template('./user.html',name=user,email=email)
    
    else:
        flash(f"You are not logged in ,please log in to continue",'info')
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    if "user" in session:
        user= session["user"]
        flash(f"You've been logged out successfully {user}","info")
    session.pop("user", None)
    session.pop("email",None)
    return redirect(url_for("login"))



@app.route('/example')
def example():
    return render_template('./example.html',ere=er)


    

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)




# in the terminal of this file path ,type - python app.py to start development server.
#Go to the server address provided to see the results.