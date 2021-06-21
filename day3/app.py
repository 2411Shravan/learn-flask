from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
#condition declaation
a = False

names= ['shravan','shreyas','praveen','pradyumna','chandan','ashik']
er = 'right'


@app.route('/')
@app.route('/home')
def home():
    return render_template('./index.html',ere=er)

@app.route('/example')
def example():
    return render_template('./example.html',ere=er)


    

if __name__ == '__main__':
    app.run(debug=True)




# in the terminal of this file path ,type - python app.py to start development server.
#Go to the server address provided to see the results.