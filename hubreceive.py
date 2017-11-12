import json

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=["POST"])
def HubReceive():

       if request.method == "POST":
               json_dict = request.get_json()

               tempAmount = json_dict['temperature']
               data = {'temperature': tempAmount, 'temperature': tempAmount}
               print(data)
               return jsonify(data)
       else:

               return """<html><body>
               Something went horribly wrong
               </body></html>"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
