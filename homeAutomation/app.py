from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template, url_for, request
#from rpi_rf import RFDevice
#import Adafruit_DHT as dht
from homeAutomation.help.graph_generator import GraphTemp
import datetime

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

g = GraphTemp()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class sensors(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    date = db.Column('date', db.DateTime, default=datetime.datetime.now)
    temp = db.Column(db.String(4), nullable=False)
    hum = db.Column(db.String(4), nullable=False)

    def __init__(self, date, temp, hum):
        self.date = date
        self.temp = temp
        self.hum = hum

    def get_temperature(self):
        return self.temp

    def get_humudity(self):
        return self.hum

    def get_time(self):
        return str(self.date)
db.create_all()



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
    temp = [temp.get_temperature() for temp in sensors.query.all()]
    time = [time.get_time() for time in sensors.query.all()]

    name = g.create(time, temp)
    print(temp)
    print(time)
    t, h = ('10','40')
    """
    h,t = dht.read_retry(dht.DHT22,4)
    h = '{0:0.1f}*C'.format(h)
    t = '{0:0.1f}*C'.format(t)
    """
    return render_template('temperature.jinja',temp=t, hum=h, graph_name=name)

@app.route('/setblind', methods=['GET','POST'])
def set_blinds():
    return render_template('blind_control.jinja')

@app.route('/admin', methods=['GET','POST'])
def admin():
    return render_template('admin.jinja')

if __name__ == "__main__":
    app.run(debug=True)
