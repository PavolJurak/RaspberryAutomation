from flask import render_template, url_for, request
from homeAutomation import app
from homeAutomation.help.graph_generator import GraphTemp
from homeAutomation import session
from homeAutomation.models import SensorsData
from homeAutomation.help.help import clear_graph_files
from datetime import datetime

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

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.jinja')


@app.route("/led")
def led_control():
    return render_template('led_control.jinja')


@app.route("/control_light", methods=['GET'])
def control_light():
    for light, code in command_codes.items():
        if request.args.get(light) is not None:
            for status, rf_code in code.items():
                if request.args.get(light) == status:
                    print('Svetlo: ', light, 'code:',rf_code)
                    #send_rf_code(int(rf_code))
    return render_template('temperature.jinja')


@app.route('/setlight', methods=['GET'])
def set_lights():
    if request.args.get('radio_code') is not None:
        rf_code = request.args.get('radio_code')
        print(rf_code)
        return ''
    else:
        return render_template('setting_lights.jinja')


@app.route('/temperature')
def temperature():
    temperature_file = ''
    humidity_file = ''
    clear_graph_files()
    graph = GraphTemp()
    now = datetime.now().strftime('%Y-%m-%d ')
    start = datetime.now().strftime('%Y-%m-%d ') + '00:00:00'
    end = now + '23:59:59'
    values = session.query(SensorsData).filter(SensorsData.date >= start).all()
    temp = [value.get_temperature() for value in values]
    hum = [value.get_humidity() for value in values]
    time = [value.get_time() for value in values]
    print(temp, hum, time)
    t, h = ('10','40')
    temperature_file = graph.createTemperature(time,temp)
    humidity_file = graph.createHumidity(time,hum)
    """
    h,t = dht.read_retry(dht.DHT22,4)
    h = '{0:0.1f}*C'.format(h)
    t = '{0:0.1f}*C'.format(t)
    """
    return render_template('temperature.jinja',temp=t, hum=h, temperature_file=temperature_file, humidity_file=humidity_file)


@app.route('/setblind', methods=['GET','POST'])
def set_blinds():
    return render_template('blind_control.jinja')


@app.route('/admin', methods=['GET','POST'])
def admin():
    return render_template('admin.jinja')


@app.teardown_appcontext
def cleanup(resp_or_exc):
    session.remove()

if __name__ == "__main__":
    app.run(debug=True)
