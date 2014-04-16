import os
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hello.html')

if __name__ == '__main__':
	app.run()