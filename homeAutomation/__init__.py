from flask import Flask
from .db import session
from homeAutomation.help.graph_generator import GraphTemp

app = Flask(__name__)