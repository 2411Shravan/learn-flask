from flask import Flask, redirect, url_for


app = Flask(__name__)
#condition declaation
a = False

@app.route('/')
@app.route('/index')
def home():
    return "<h1>Hello World</h1>"


@app.route('/<name>')

def user(name):
    
    return f"Hello {name}"


@app.route('/admin')
def admin():
    
    if (a):
#check for condition of a and if it is true then user will be directed to home page otherwise into the admin panel
        return redirect(url_for("home"))
    else:
        return "<h1>You're in the admin section</h1>"

if __name__ == '__main__':
    app.run(debug=True)




# in the terminal of this file path ,type - python app.py to start development server.
#Go to the server address provided to see the results.