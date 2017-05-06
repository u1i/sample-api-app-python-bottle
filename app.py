from bottle import default_app, route, response, run
from random import randint

# from json import dumps

# @route('/')
# def hello_world():
#     return 'Hello from Bottle!'

@route('/api-request')
def returnarray():
    rv = [{ "id": 1, "random": randint(1000,9999), "attempts":"37" }, { "id": 2, "random": randint(1000,9999) }]
    return dict(data=rv)

application = default_app()

run(server='wsgiref', host="0.0.0.0", port=8080)

