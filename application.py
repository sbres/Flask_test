import logging
import logging.handlers
import json
from pynamodb.models import Model
import pynamodb.attributes as db
from pynamodb.exceptions import DoesNotExist
# Create logger
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

class Data(Model):
    class Meta:
        table_name = 'data'
        #host = "http://localhost:6969"
    key = db.UnicodeAttribute(hash_key=True)
    uid = db.NumberAttribute(range_key=True)
    data = db.JSONAttribute()


@application.route('/get', methods=['GET'])
def get_key():
    if not Data.exists():
        return ''
    to_check = ['id', 'key']
    for element in to_check:
        if request.args.get(element) is None:
            return ''
    id = int(request.args.get('id'))
    key = request.args.get('key')
    try:
        item = Data.get(key, id)
    except DoesNotExist:
        return ''
    return item.data

@application.route('/put', methods=['POST'])
def set_key():
    if not Data.exists():
        logging.info('Creating table')
        Data.create_table(wait=True, read_capacity_units=1, write_capacity_units=1)
    to_check = ['id', 'key', 'value']
    if request.method == 'POST':
        for element in to_check:
            if request.form.get(element) is None:
                return '{0} not in request.'.format(element)
            #print '{0} is here'.format(request.form.get(element))
    else:
        'This is a POST request.'
    id = int(request.form.get('id'))
    key = request.form.get('key')
    _value = request.form.get('value')
    value = json.dumps(_value)
    item = Data(key, id, data=value)
    item.save()
    return 'OK'


if __name__ == '__main__':
    application.debug = True

    application.run(host='0.0.0.0', port=8000, threaded=True)
    #application.run()
