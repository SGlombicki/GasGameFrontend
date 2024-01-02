from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def updater():  # put application's code here
	os.system('systemctl restart updater.service')
	return 'Updating...'

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

if __name__ == '__main__':
	app.run()
