import datetime
from homeAutomation.app import db, sensors

def save_to_db(temp, hum):
    now = datetime.datetime.now()
    sensor = sensors(now, temp, hum)
    db.session.add(sensor)
    db.session.commit()

if __name__ == '__main__':
    temp = '80'
    hum = '80'
    save_to_db(temp,hum)
