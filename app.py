from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/contato.html')
def contato():
    return render_template("contato.html")


@app.route('/quem.html')
def quem():
    return render_template("quem.html")

if __name__ == '__main__':
    app.run(debug = True)