from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from museum_main import app, db
from museum_main.models_building import *
from museum_main.models_imgs import *
from museum_main.models import *


@app.route('/')
def hello_world():
    return redirect(url_for('show_villages'))


@app.route('/jxgd')
def show_villages():
    villages = Village.query.all()
    return render_template('show_villages.html', villages=villages)


@app.route('/jxgd/add_village', methods=['POST'])
def add_village():
    if not session.get('logged_in'):
        abort(401)

    village_name = request.form['village_name']
    village_text = request.form['village_text']
    new_village = Village(village_name, village_text)
    db.session.add(new_village)

    # TODO
    # Move commit() to other place
    db.session.commit()
    flash('New village was successfully posted')
    return redirect(url_for('show_villages'))


#----------------------------------------------------#
#     login / logout management                      #
#----------------------------------------------------#

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_villages'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_villages'))