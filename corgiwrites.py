from flask import (
    Flask,
)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def front():
    return """<h1>Hello world!</h1>
    <small>corgi and fox</small>"""

@app.route('/makyo')
def makyo():
    return "Foxes!"

if __name__ == '__main__':
    app.run()
