from backend.auth import auth
from flask import render_template,session, request,redirect,url_for,flash,current_app,make_response


@auth.route('/login',methods=['GET','POST'])
def login():
    print('login')
    return render_template('base.html')


@auth.route('/logout',methods=['GET','POST'])
def logout():
    print('login')
    return render_template('base.html')