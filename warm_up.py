# import the Flask class from the flask module
from flask import Flask
# creates a flash app object
app = Flask('MyApp')

@app.route('/')
def hello():
    return '<h1>Hello world!</h1>'
# start the server if run on the command line
if __name__ == '__main__':
    app.run(debug=True)
