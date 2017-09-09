from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash, jsonify

import sqlite3
import datetime

import blinkpy

app = Flask(__name__)
app.config.from_object('config')


def setup_blink():
	blink = blinkpy.Blink(username=app.config['BLINK_USERNAME'], password=app.config['BLINK_PASSWORD'])
	blink.setup_system()
	return blink

@app.before_request
def before_request():
	g.blink = setup_blink()

# @app.teardown_request
# def teardown_request(exception):
# 	pass


@app.route('/')
def index():
	output = {}
	for name, camera in g.blink.cameras.items():
	    # print(name)                  # Name of the camera
	    # print(camera.id)             # Integer id of the camera (assigned by Blink)
	    # print(camera.armed)          # Whether the device is armed/disarmed (ie. detecting motion)
	    # print(camera.clip)           # Link to last motion clip captured
	    # print(camera.thumbnail)      # Link to current camera thumbnail
	    # print(camera.temperature)    # Current camera temperature (not super accurate, but might be useful for someone)
	    # print(camera.battery)        # Current battery level... I think the value ranges from 0-3, but not quite sure yet.
	    # print(camera.battery_string) # Gives battery level as a string ("OK" or "Low").  Returns "Unknown" if value is... well, unknown
	    # print(camera.notifications)  # Number of unread notifications (ie. motion alerts that haven't been viewed)
	    # print(camera.motion)         # Dictionary containing values for keys ['video', 'image', 'time']
	    # print(camera.image_link)     #
	    # #print(camera.video_link)     # 
	    # 							 # which corresponds to last motion recorded, thumbnail of last motion, and timestamp of last motion

	    output[camera.id] = {
	    	'id': camera.id,
	    	'name': name,
	    	'armed': camera.armed,
	    	'clip': camera.clip,
	    	'thumbnail': camera.thumbnail,
	    	'temperature': camera.temperature,
	    	'battery': camera.battery,
	    	'battery_string': camera.battery_string,
	    	'notifications': camera.notifications,
	    	'motion': camera.motion,
	    	'image_link': camera.image_link

	    }

	return jsonify(output)

