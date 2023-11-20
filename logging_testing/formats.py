import json
import logging
import re
import requests


class JSONTo(logging.Formatter):
    def __init__(self) -> None:
        
        super(JSONTo, self).__init__()

    def format(self, record):
        regex=re.compile('Password : [A-Za-z0-9@#$%^&+=,\.]')
        if regex.match(record.msg):
            record.msg=re.sub('[A-Za-z0-9@#$%^&+=,\.]', '*', record.msg)
        data = {'data': record.msg,                
                    'funcName' : record.funcName,
                    'lineno' : record.lineno,
                    'exc_info' : record.exc_info, 
                    'exc_text' : record.exc_text,                 
                    }           

        return json.dumps(data)



class CustomFormatter(logging.Formatter):

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    


class RequestsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        return requests.post('https://webhook.site/9e0fb6ee-498b-41e0-a4cf-b439a8432d23', log_entry, headers={"Content-type": "application/json"}).content