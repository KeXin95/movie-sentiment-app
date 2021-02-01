from flask import request, jsonify
from flask import current_app as app
from flask_cors import cross_origin
from misc.heuristic import AIModel
from misc.explainer import Explainer
# import os

model = AIModel()
explainer = Explainer()


@cross_origin()
@app.route('/scan', methods=['GET'])
def echo():
    # os.remove('/Users/kexinchong/Downloads/frontend/frontend/public/app/temp.html')
    sentence = request.args.get("sentence")
    sentiment = model.predict(sentence)
    result_json = jsonify({'result': sentiment})
    return result_json


@cross_origin()
@app.route('/explain', methods=['GET'])
def expl():
    sentence = request.args.get("sentence")
    status = explainer.explain(sentence)
    result_json = jsonify({'result': status})
    return result_json
