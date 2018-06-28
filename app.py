from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.route('/slack/receiverequest', methods=["POST"])
def listenforrequest():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":"application/json"})
