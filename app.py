from flask import Flask, json, request
from uuid import uuid4
from calc import addition, subtraction, multiplication, division, factorial

app = Flask(__name__)
API_KEY = "chavedaaqms"

'''
curl -X POST -H "apiKey: chavedaaqms" -H "Content-Type: application/json" \
    -d '{"value": 0, "add": 50}' \
    http://127.0.0.1:5000/add

{"result": 50}%      
'''

def jsonResponse(code, data):
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )

def isValidApikey(apiKey):
    if apiKey == API_KEY:
        return True
    else:
        return False


@app.route("/")
def hello_world():
    return "<p>AQMS Calculator API</p>"


@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        try:
            if isValidApikey(request.headers['apiKey']) is False:
                return jsonResponse(400, "Api key is not valid!")

            body = request.get_json()
            value = body['value']
            add = body['add']

            result = addition(value, add)

            data = {
                "result": result
            }
            response = jsonResponse(200, data)

        except Exception as e:
            response = jsonResponse(400, e.__class__)

        finally:
            return response


@app.route("/sub", methods=['POST'])
def sub():
    if request.method == 'POST':

        try:
            if isValidApikey(request.headers['apiKey']) is False:
                return jsonResponse(400, "Api key is not valid!")

            body = request.get_json()
            value = body['value']
            sub = body['sub']

            result = subtraction(value, sub)

            data = {
                "result": result
            }
            response = jsonResponse(200, data)

        except Exception as e:
            response = jsonResponse(400, e.__class__)

        finally:
            return response


@app.route("/mult", methods=['POST'])
def mult():
    if request.method == 'POST':
        try:
            if isValidApikey(request.headers['apiKey']) is False:
                return jsonResponse(400, "Api key is not valid!")

            body = request.get_json()
            value = body['value']
            mult = body['mult']

            result = multiplication(value, mult)

            data = {
                "result": result
            }
            response = jsonResponse(200, data)

        except Exception as e:
            response = jsonResponse(400, e.__class__)

        finally:
            return response


@app.route("/div", methods=['POST'])
def div():
    if request.method == 'POST':
        try:
            if isValidApikey(request.headers['apiKey']) is False:
                return jsonResponse(400, "Api key is not valid!")

            body = request.get_json()
            value = body['value']
            div = body['div']

            result = division(value, div)

            data = {
                "result": result
            }
            response = jsonResponse(200, data)

        except Exception as e:
            response = jsonResponse(400, e.__class__)

        finally:
            return response

@app.route("/factorial", methods=['POST'])
def fact():
    if request.method == 'POST':
        try:
            if isValidApikey(request.headers['apiKey']) is False:
                return jsonResponse(400, "Api key is not valid!")

            body = request.get_json()
            value = body['value']

            result = factorial(value)

            data = {
                "result": result
            }
            response = jsonResponse(200, data)

        except Exception as e:
            response = jsonResponse(400, e.__class__)

        finally:
            return response