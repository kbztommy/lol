from jinja2 import Markup
from datetime import datetime

def time_format_filter(s):
    return datetime.fromtimestamp(s/1000)
