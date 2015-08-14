import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash
from contextlib import closing

DATABASE = 'tmp/ship.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__, static_url_path='/static/')
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/add', methods=['POST'])
def add_delivery():
    g.db.execute('insert into deliveries (tracking, carrier, '
                 'street_address, zipcode) values (?, ?, ?, ?)',
                 [request.form['tracking'], request.form['carrier'],
                  request.form['street_address'], request.form['zipcode']])
    g.db.commit()
    flash('Delivery added')
    return redirect(url_for('show_deliveries'))


@app.route('/')
def show_deliveries():
    cur = g.db.execute('select tracking, carrier, street_address, zipcode from'
                       ' deliveries order by zipcode desc')
    deliveries = [dict(tracking=row[0], carrier=row[1], street_address=row[2],
                       zipcode=row[3])
                  for row in cur.fetchall()]
    return render_template('index.html', deliveries=deliveries)


if __name__ == '__main__':
    app.run()
