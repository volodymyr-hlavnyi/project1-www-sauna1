from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# @app.route('/age-calculator', methods=["GET", "POST"])
# def index():
#     return render_template('age-calculator.html')


#For base and page2 html


@app.route('/')
def base():

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6200, debug=False)