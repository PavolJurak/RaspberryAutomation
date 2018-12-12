from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from db import engine
from datetime import datetime

Base = declarative_base()

class SensorsData(Base):
    __tablename__ = 'sensors_data'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
    temperature = Column(String, nullable=False)
    humidity = Column(String, nullable=False)

    def __init__(self, date, temperature, humidity):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_time(self):
        return self.date.strftime('%H:%M')

    def __repr__(self):
        return "<Message(date={0}, temperature={1}, humidity={2})>".format(self.date, self.temperature, self.humidity)

Base.metadata.create_all(engine)