from flask import Flask
from flask import render_template, url_for, request
#from rpi_rf import RFDevice
from help.graph_generator import GraphTemp

command_codes = {'B_Light1': {'ON': '5393', 'OFF': '5293'},
                'B_Light2': {'ON': '5193', 'OFF': '5093'},
                'AllBedroomLights': {'ON': '5593', 'OFF': '5493'},
                'L_Light1': {'ON': '4993', 'OFF': '4893'},
                'L_Light2': {'ON': '4793', 'OFF': '4693'},
                'L_Light3': {'ON': '4593', 'OFF': '4493'},
                'L_Light4': {'ON': '4193', 'OFF': '4293'},
                'AllLivingRoomLights': {'ON': '4093', 'OFF': '3993'},
                'Garden': {'ON': '3893', 'OFF': '3793'}
                 }

lights = [light_name for light_name in command_codes.keys()]


def send_rf_code(code):
    pass
    """
    rf_pin = 17
    rfdevice = RFDevice(rf_pin)
    rfdevice.enable_tx()
    rfdevice.tx_code(code,1,350)
    """
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.jinja')

@app.route("/control_light", methods=['GET'])
def control_light():
    for light, code in command_codes.items():
        if request.args.get(light) is not None:
            for status, rf_code in code.items():
                if request.args.get(light) == status:
                    print('Svetlo: ', light, 'code:',rf_code)
                    #send_rf_code(int(rf_code))
    return ''

@app.route('/led')
def led_lamp():
    return render_template('home.jinja')

@app.route('/temperature')
def temperature():
    g = GraphTemp()
    g.create()
    return render_template('temperature.jinja')

@app.route("/setlight",methods=['GET'])
def set_lights():
    if request.args.get('radio_code') is not None:
        rf_code = request.args.get('radio_code')
        print(rf_code)
        return ''
    else:
        return render_template('setting_lights.jinja')


if __name__ == "__main__":
    app.run(debug=True)
