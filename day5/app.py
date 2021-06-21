from flask import Flask, redirect, url_for, render_template, request,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key="shravan_erefre"
app.permanent_session_lifetime = timedelta(days=2)

a = False

names= ['shravan','shreyas','praveen','pradyumna','chandan','ashik']
er = 'right'


@app.route('/')
@app.route('/home')
def home():
    return render_template('./index.html',ere=er)


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nam']
        session['user'] = user
        return redirect(url_for("user"))
    else:

        if "user" in session:
            return redirect(url_for("user"))
        return render_template('./login.html')


@app.route("/user/")
def user():    
    if "user" in session :
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



@app.route('/example')
def example():
    return render_template('./example.html',ere=er)


    

if __name__ == '__main__':
    app.run(debug=True)




# in the terminal of this file path ,type - python app.py to start development server.
#Go to the server address provided to see the results.