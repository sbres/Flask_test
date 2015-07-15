import logging
import logging.handlers
import json

#############   TORNADO IMPORTS   ############
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
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
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Coucou ^.^'

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(application))
    http_server.listen(8000)
    IOLoop.instance().start()


