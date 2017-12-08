import json, datetime, os

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
					'temperature': 'null',
					'sound': 'null',
					'humidity': 'null',
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Light Measurement': measurement,
					'Temperature measurement': 'null',
					'Sound Measurement': 'null',
					'Humidity Measurement': 'null'
				})			

			if piId == 2:
				tempAmount = json_dict['temperature']
				data['data'].append({
					'light': 'null',
					'temperature': tempAmount, 
					'sound': 'null',
					'humidity': 'null',
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Light Measurement': 'null',
					'Temperature measurement': measurement,
					'Sound Measurement': 'null',
					'Humidity Measurement': 'null'
				})	
		
			elif piId == 5:
				humidityAmount = json_dict['humidity']
				data['data'].append({
					'humidity': humidityAmount, 
					'light': 'null',
					'temperature': 'null', 
					'sound': 'null',
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Light Measurement': 'null',
					'Temperature measurement': 'null',
					'Sound Measurement': 'null',
					'Humidity Measurement': measurement
				})

			elif piId == 3:
				soundStatus = json_dict['sound']
				data['data'].append({
					'sound': soundStatus,
					'humidity': 'null', 
					'light': 'null',
					'temperature': 'null', 
					'pi id': piId, 
					'team id': teamId, 
					'Time': currentTime, 
					'Date': currentDate, 
					'Light Measurement': 'null',
					'Temperature measurement': 'null',
					'Sound Measurement': measurement,
					'Humidity Measurement': 'null'
				})
			
			print(data)
			
			with open('data.json', 'w') as outfile:
				json.dump(data, outfile)
			
			os.system('./pushScript.sh')

			return jsonify(data)
	else:

		return """<html><body>
		Something went horribly wrong
		</body></html>"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
