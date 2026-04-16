from flask import Flask, render_template, Response, request
import RPi.GPIO as GPIO
import io
import picamera
from threading import Condition, Thread

app = Flask(__name__)

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

pwm = GPIO.PWM(17, 100)
pwm.start(50)
pmw = GPIO.PWM(22, 100)
pmw.start(50)

# Initialize GPIO pins
GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

# Video Streaming Output
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

output = StreamingOutput()

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML file for the interface

@app.route('/stream.mjpg')
def stream():
    def generate():
        while True:
            with output.condition:
                output.condition.wait()
                frame = output.frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    if action == 'up':
        pwm.ChangeDutyCycle(50)
        GPIO.output(18, GPIO.LOW)
        pmw.ChangeDutyCycle(50)
        GPIO.output(27, GPIO.LOW)
    elif action == 'down':
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
    return "Action performed!"

def start_camera():
    with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
        camera.start_recording(output, format='mjpeg')
        try:
            while True:
                camera.wait_recording(1)
        finally:
            camera.stop_recording()

if __name__ == '__main__':
    camera_thread = Thread(target=start_camera)
    camera_thread.daemon = True
    camera_thread.start()
    app.run(host='0.0.0.0', port=8000, threaded=True)
