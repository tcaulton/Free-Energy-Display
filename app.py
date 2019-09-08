# app.py

from flask import Flask
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import calculationModule

app = Flask(__name__)



@app.route('/')
def my_form():
	return render_template('testPage.html')
def dynamic_page():
	return calculationModule.graph()


	

@app.route('/<name>')
def index(name):
	return '<h1>Hello! {}!</h1>'.format(name)
	





	

