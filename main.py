from flask import Flask
from flask import render_template


DEBUG = False
DEBUG = True

app = Flask(__name__)


@app.route("/")
@app.route("/projector/")
def page_projector():
    return render_template('projector.html')


@app.route('/control/')
def page_control():
    return render_template('control.html')


if __name__ == "__main__":  
    app.run(host="0.0.0.0", debug=DEBUG)

