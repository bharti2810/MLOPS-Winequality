from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction

params_path ="params.yaml"
webapp_root="webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder = static_dir, template_folder=template_dir)

# def api_response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            print("request.method",request.method)
            if request.form:# if request is coming from web app
                data_req = dict(request.form)
                response = prediction.form_response(data_req)
                return render_template("index.html",response=response)# becvause we are using same page for result also
            elif request.json: # if request coming from an api not from form method so it can tested from postman also
                response = prediction.api_response(request.json)
                return jsonify(response)
        except Exception as e:
            print(e)
            # this error dictionary required in 404.html
            return render_template("404.html",error=e)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)
