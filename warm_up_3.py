# import the Flask class from the flask module
from flask import Flask, render_template
import pg

db = pg.DB(dbname='restaurant_db')
# creates a flash app object
app = Flask('MyApp')

@app.route('/')
def projects():
    query = db.query('select * from restaurant')

    return render_template(
        'index.html',
        title='Restaurants',
        restaurant_list = query.namedresult()
    )
# start the server if run on the command line
if __name__ == '__main__':
    app.run(debug=True)
