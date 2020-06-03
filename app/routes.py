from app import app
from .controller import *

app.add_url_rule("/", "index", index)
