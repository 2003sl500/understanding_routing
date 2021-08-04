from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:repeat>/<word>')
def repeat(word, repeat):
    return word * repeat

if __name__ == "__main__":
    app.run(debug=True)