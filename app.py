from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/angebote')
def angebote():
    return render_template('angebote.html', title='Angebote')


@app.route('/preise')
def preise():
    return render_template('preise.html', title='Preise')


@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', title='Kontakt')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6200, debug=True)
