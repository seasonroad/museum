import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, config
from werkzeug import secure_filename
import time
import os
import PIL
from museum_main import app, db
from museum_main.models_building import *
from museum_main.models_imgs import *
from museum_main.models import *
from museum_main.serialize import serialize


@app.teardown_request
def teardown_request(exception):
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()

@app.route('/test/')
def test():
    return render_template('test-popup.html')


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

    flash('New village was successfully posted')
    return redirect(url_for('show_villages'))


#=======================================================#
#                     Village Page                      #
#=======================================================#
@app.route('/jxgd/village/<int:village_id>', methods=['GET'])
def show_village(village_id):
    village = db.session.query(Village).get(village_id)
    villages = db.session.query(Village).all()
    print villages
    return render_template('villages/village.html', village=village, villages=villages)


@app.route('/jxgd/upload_list', methods=['POST', 'GET'])
def what():
    print request
    if request.method == 'POST':
        req_f = request.files[u'files[]']
        villiage_id = int(request.form[u'village_id'])
        if req_f:
            filename = secure_filename(req_f.filename)
            suffix = os.path.splitext(filename)[-1]
            filename = str(int(time.time()*10000))+suffix
            file_path_ori = os.path.join(app.config['PIC_DIR'], filename)
            file_path_thumb = os.path.join(app.config['PIC_THUMB_DIR'], filename)
            # Add to DB
            new_image = BuildingImg(filename, '', file_path_ori, file_path_thumb)
            new_image.save(req_f)
            new_image.save_thumb()
            if villiage_id:
                new_image.village_id = villiage_id
            db.session.add(new_image)
            db.session.flush()

            files = serialize(new_image)
            r = {'files':[files]}
            print r
            return json.dumps(r)
        else:
            pass

    if request.method == 'GET':
        return json.dumps('')


@app.route('/jxgd/delete/pic', methods=['POST', 'GET'])
def picture_delete():
    pass


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