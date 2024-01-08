from backend.main import main
from backend.extensions import bcrypt,db,mail,Message,csrf,cache
from flask import render_template,session, request,redirect,url_for,flash,current_app,make_response


@main.route('/',methods=['GET','POST'])
def homepage():
    return render_template('homepage.html')