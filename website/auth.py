from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import datetime

auth = Blueprint('auth', __name__) 


def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour
    first_name = request.form.get('firstName')
    

    if currentTime.hour < 12:
        greet = f"Good morning {first_name}, may I get your reminders for you?"
        return greet
    elif 12 <= currentTime.hour < 16:
        greet = f"Good afternoon {first_name}, Can you feel the weather!?"
        return greet
    else:
        greet = f"Good Evening {first_name}, would you like to have a cup of coffee?"
        return greet
  
  
    
def greeting_user():
    currentTime = datetime.datetime.now()
    currentTime.hour
    

    if currentTime.hour < 12:
        greet = f"Good morning, may I get your reminders for you?"
        return greet
    elif 12 <= currentTime.hour < 16:
        greet = f"Good afternoon, Can you feel the weather!?"
        return greet
    else:
        greet = f"Good Evening, would you like to have a cup of coffee?"
        return greet





@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('firstName')
        
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f'Logged in successfully! {greeting_user()}', category="success")
                
                # logout_user()
                login_user(user, remember=True)
                
                
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect user details, try again', category="error")
        else:
            flash('Email does not exist exist.', category="error")
            
                
                          
    return render_template('login.html', user=current_user)










@auth.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))









@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category="error")
        # elif email == "" or first_name == "" or last_name == "" or password1 == "" or password2 == "":
        #     flash('Forms must not be empty!!', category="error")
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category="error")
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters', category="error")
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 characters', category="error")
        elif password1 != password2:
            flash('Password don\'t match', category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category="error")
        else:
            # add user to the database
            new_user = User(email=email, first_name=first_name,  password=generate_password_hash(password1, method = 'sha256'))
            
            db.session.add(new_user)
            db.session.commit()
            
            # logout_user()
            login_user(new_user, remember=True)
            
            
            flash(f'Account created successfully {greeting()}', category="success")
            return redirect(url_for('views.home'))
            
    return render_template('sign_up.html', user=current_user)



