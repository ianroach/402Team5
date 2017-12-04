import json, datetime

from flask import Flask, request, jsonify

now = datetime.datetime.now()
app = Flask(__name__)
@app.route('/', methods=["POST"])
def HubReceive():
	
	while True:
		if request.method == "POST":
			json_dict = request.get_json()
		
			tempAmount = json_dict['temperature']
			piId = json_dict['pi id']
			teamId = json_dict['team id']
			currentTime = json_dict['currentTime']
			currentDate = json_dict['currentDate']
			measurement = json_dict['Measurement']
		
			data = {'temperature': tempAmount, 'pi id': piId, 'team id': teamId, 'Time': currentTime, 'Date': currentDate, 'Measurement': measurement}
			print(data)
			with open('data.txt', 'a') as outfile:
				json.dump(data, outfile)
				outfile.write('\n')
			return jsonify(data)
		else:

			return """<html><body>
			Something went horribly wrong
			</body></html>"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
