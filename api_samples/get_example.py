from flask import request
from flask_lambda import FlaskLambda
import json

app = FlaskLambda(__name__)

@app.route('/hello', methods=['GET'])
def get_Hello():
    
    try:
        # Construct the body of the response Object
    
        transResponse = {}
        transResponse['transId'] = 100
        transResponse['transType'] = 'SALE'
        transResponse['transAmt'] = 200
        transResponse['message'] = 'Hello from Lambda Land'
        
        
        ## Construct Http Response Object
        responseObject = {}
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(transResponse)
        
        # return the response object
        return responseObject
        #return json.loads(json_data)
    except Exception as e:
        return {"Status Code": 404,"error_message": "error: {}".format(e)}



