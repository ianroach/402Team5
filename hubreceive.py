import json, datetime

from flask import Flask, request, jsonify

now = datetime.datetime.now()


app = Flask(__name__)
@app.route('/', methods=["POST"])
def HubReceive():
	
	data = {}
	data['data'] = []
	

	if request.method == "POST":
		counter = input("how many data points do you want?")
		for x in range(int(counter)):
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
				#data['data'] = []
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
				data = {'temperature': tempAmount, 'pi id': piId, 'team id': teamId, 'Time': currentTime, 'Date': currentDate, 'Measurement': measurement}
			elif piId == 5:
				humidityAmount = json_dict['humidity']
				data = {'humidity': humidityAmount, 'pi id': piId, 'team id': teamId, 'Time': currentTime, 'Date': currentDate, 'Measurement': measurement}
			elif piId == 3:
				soundStatus = json_dict['sound']
				data = {'sound': soundStatus, 'pi id': piId, 'team id': teamId, 'Time': currentTime, 'Date': currentDate, 'Measurement': measurement}
			#elif piId == 4:
				#lightStatus = json_dict['light']
				#data = {'light': lightStatus, 'pi id': piId, 'team id': teamId, 'Time': currentTime, 'Date': currentDate, 'Measurement': measurement}
			print(data)
			#with open('data.json', 'a') as outfile:
				#json.dump(data, outfile)
				#outfile.write('\n')
		with open('data.json', 'a') as outfile:
			json.dump(data, outfile)
			outfile.write('\n')
			return jsonify(data)
	else:

		return """<html><body>
		Something went horribly wrong
		</body></html>"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
