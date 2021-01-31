from flask import request, jsonify
from flask import current_app as app
from flask_cors import cross_origin
from misc.heuristic import AIModel
from misc.explainer import Explainer
# import os

model = AIModel()
explainer = Explainer()


@cross_origin()
@app.route('/echo', methods=['GET'])
def echo():
    # os.remove('/Users/kexinchong/Downloads/frontend/frontend/public/app/temp.html')
    hashtag = request.args.get("hashtag")
    sentiment = model.predict(hashtag)
    result_json = jsonify({'result': sentiment})
    return result_json


@cross_origin()
@app.route('/explain', methods=['GET'])
def expl():
    hashtag = request.args.get("hashtag")
    exp = explainer.explain(hashtag)
    result_json = jsonify({'result': exp})
    return result_json
