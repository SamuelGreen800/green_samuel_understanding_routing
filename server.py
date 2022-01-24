from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/Dojo')
def success():
    return "Dojo!"


@app.route('/say/<string:name>')
def say_stuff(name):
    return f"Hi {name}"



@app.route('/hello/<string:phrase>/<int:num>')
def hello(num, phrase):
    return f"Hello {phrase * num}"




if __name__=="__main__":
    app.run(debug=True)
