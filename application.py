import logging
import logging.handlers
import json
import time
#############   TORNADO IMPORTS   ############
from gevent.wsgi import WSGIServer

############# END TORNADO IMPORTS ############


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
#handler.setFormatter(formatter)

# add Handler to Loggers
#logger.addHandler(handler)

from flask import Flask, request
_application = Flask(__name__)

@_application.route('/')
def hello_world():
    #gevent.sleep(0.3)
    return 'Coucou ^..^'
_application.debug = True

application = WSGIServer(('', 8000), _application)

if __name__ == '__main__':
    http_server = WSGIServer(('', 8000), application)
    http_server.serve_forever()



