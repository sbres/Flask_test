import logging
import logging.handlers
import json
import newrelic.agent
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
    #application = myapp.WSGIHandler()
    application = newrelic.agent.WSGIApplicationWrapper(application)


    application.debug = True
    application.run(host='0.0.0.0', port=8000)
    #application.run()
    #application.run()
