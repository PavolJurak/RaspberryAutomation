from flask import Flask
from flask import render_template, url_for, request
from rpi_rf import RFDevice
from help.graph_generator import GraphTemp

command_codes = {'B_Light1': {'ON': '5393', 'OFF': '5293'},
                'B_Light2': {'ON': '5193', 'OFF': '5093'}
                }
lights = [light_name for light_name in command_codes.keys()]


def send_rf_code(code):
    rf_pin = 17
    rfdevice = RFDevice(rf_pin)
    rfdevice.enable_tx()
    rfdevice.tx_code(code,1,350)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.jinja')

@app.route("/control_light", methods=['GET'])
def control_light():
    if request.args.get('B_Light1') is not None:
        value = request.args.get('B_Light1')
        if value == 'ON':
            send_rf_code(5393)
        elif value == 'OFF':
            send_rf_code(5293)

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
