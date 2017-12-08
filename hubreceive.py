import json, datetime, subprocess

from flask import Flask, request, jsonify

now = datetime.datetime.now()


app = Flask(__name__)
@app.route('/', methods=["POST"])
def HubReceive():
	
	with open('data.json') as json_data:
		data = json.load(json_data)
	
	while True:

		if request.method == "POST":

			json_dict = request.get_json()
		
			#tempAmount = json_dict['temperature']
			#humidityAmount = json_dict['humidity']
			#soundStatus = json_dict['sound']
			#lightStatus = json_dict['light']
			piId = json_dict['pi id']
			teamId = json_dict['team id']
			currentTime = json_dict['currentTime']
			currentDate = json_dict['currentDate']
			measurement = json_dict['Measurement']
			

			if piId == 4:
				lightStatus = json_dict['light']
				data['data'].append({
					'light': lightStatus, 
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Measurement': measurement
				})			

			if piId == 2:
				tempAmount = json_dict['temperature']
				data['data'].append({
					'temperature': tempAmount, 
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Measurement': measurement
				})	
		
			elif piId == 5:
				humidityAmount = json_dict['humidity']
				data['data'].append({
					'humidity': humidityAmount, 
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Measurement': measurement
				})

			elif piId == 3:
				soundStatus = json_dict['sound']
				data['data'].append({
					'sound': soundStatus, 
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Measurement': measurement
				})
			
			print(data)
			
			with open('data.json', 'w') as outfile:
				json.dump(data, outfile)
			

			return jsonify(data)
	else:

		return """<html><body>
		Something went horribly wrong
		</body></html>"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
