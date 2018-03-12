from flask import Flask, render_template, Response, jsonify
import os
from time import sleep
import math
import threading
import sensors

# emulated camera
#from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)

global panServoAngle
global tiltServoAngle
panServoAngle = 90
tiltServoAngle = 90

panPin = 27
tiltPin = 17

@app.route('/')
def index():
    """Video streaming home page."""
    templateData = {
      'panServoAngle'	: panServoAngle,
      'tiltServoAngle'	: tiltServoAngle
	}
    return render_template('index.html', **templateData)

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/temp_feed')
def temp_feed():
    print('got HERRE!!!!!')
    array = []
    array.append(sensors.getTemp())
    array.append(sensors.getHumid())
    array.append(sensors.getVOC())
    array.append(sensors.getCO2())
    return jsonify(array)
                    
@app.route("/<servo>/<angle>")
def move(servo, angle):
	global panServoAngle
	global tiltServoAngle
	if servo == 'pan':
		if angle == '+':
			panServoAngle = panServoAngle + 10
			os.system("python3 angleServoCtrl.py " + str(panPin) + " " + str(panServoAngle))
		else: 
			panServoAngle = panServoAngle - 10
			os.system("python3 angleServoCtrl.py " + str(panPin) + " " + str(panServoAngle))		
	if servo == 'tilt':
		if angle == '+':
			tiltServoAngle = tiltServoAngle + 10
			os.system("python3 angleServoCtrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
		else:
			tiltServoAngle = tiltServoAngle - 10
			os.system("python3 angleServoCtrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
	
	templateData = {
      'panServoAngle'	: panServoAngle,
      'tiltServoAngle'	: tiltServoAngle
	}
	return render_template('index.html', **templateData)                
                    
                    
if __name__ == '__main__':
    sensors = sensors.AirQualityTempSensor()
    app.run(host='0.0.0.0', threaded=True)
    
    
