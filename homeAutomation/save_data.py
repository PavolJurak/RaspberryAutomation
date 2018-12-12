from db import session
from models import SensorsData
from datetime import datetime

data = SensorsData(datetime.now(), '1', '1')
session.add(data)
session.commit()
