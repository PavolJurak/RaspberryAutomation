from db import session
from models import SensorsData
from datetime import datetime

data = SensorsData(datetime.now(), '50', '50')
session.add(data)
session.commit()
