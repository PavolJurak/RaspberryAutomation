from flask import Flask
from flask import render_template
from rpi_rf import RFDevice
from homeAutomation.help.graph_generator import GraphTemp

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.jinja')

@app.route('/led')
def led_lamp():
    return render_template('home.jinja')

@app.route('/temperature')
def temperature():
    g = GraphTemp()
    g.create()
    return render_template('temperature.jinja')

@app.route("/setlight")
def set_lights():
    return render_template('setting_lights.jinja')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

def send_rf_code(code):
    rf_pin = 17
    rfdevice = RFDevice(rf_pin)
    rfdevice.enable_tx(code,1,350)