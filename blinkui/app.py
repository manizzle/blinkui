from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash, jsonify
import sqlite3
import datetime

DATABASE = 'blinkui.db'
DEBUG = True


app = Flask(__name__)



@app.route('/')
def index():
	return __name__