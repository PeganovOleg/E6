from flask import Flask, jsonify, request
import os
import logging
from flask_caching import Cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
cache_client = Cache(app, config={'CACHE_TYPE': 'memcached',
                           "CACHE_MEMCACHED_SERVERS": ['127.0.0.1:11211']})

@app.route("/<int:number>", methods=['GET'])
def get_fibonacci_api(number):
    number = int(number)
    stored_value = cache_client.get(number)
    if stored_value:
        logger.info("For %s stored value is used" % number)
        return jsonify({number: stored_value.decode()}), 200
    new_value = get_fibonacci(number)
    logger.info("For %s new value is calculated" % number)
    cache_client.set(number, new_value)
    return jsonify({number: new_value}), 200

@app.route('/')
def Privet():
    return 'Пивет! Укажи после слэша номер последовательности: например, "/6"'    

def get_fibonacci(number):
    if (number == 0) or (number == 1): 
        return number
    return get_fibonacci(number-1) + get_fibonacci(number-2)        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    #app.run()
