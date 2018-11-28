from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return '<h1>Dojo!</h1>'

@app.route('/say/<name>')
def hello(name):
    return (f'Hi {name}!')

@app.route('/repeat/<num>/<tex>')
def repeat(num, tex):
    return(f'<p>{tex}</p>')*int(num)

if __name__=="__main__":
    app.run(debug=True)
