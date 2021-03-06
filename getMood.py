


import requests
import json


def getMood():
	subscription_key = '4f195ee2b2c34d3fb2d565088a9c1f38'
	face_api_url = 'https://sync-me.cognitiveservices.azure.com/'+ '/face/v1.0/detect'
	#image of person's face
	image_data = open('mood.jpg', 'rb').read()
	headers = { 'Ocp-Apim-Subscription-Key': subscription_key,
				'Content-Type': 'application/octet-stream' }
	params = { 'returnFaceId': 'false',
    		   'returnFaceLandmarks': 'false',
    		   'returnFaceAttributes': 'emotion' }

	#Uses Microsoft Azure API to read emotions from image of face
	response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
	response = response.json()
	#If API could detect a face in the image, get microemotion amounts
	if response:
		#gets all microemotion amounts
		emotions = response[0]["faceAttributes"]["emotion"]
		anger = emotions["anger"]
		contempt = emotions["contempt"]
		disgust = emotions["disgust"]
		fear = emotions["fear"]
		happiness = emotions["happiness"]
		neutral = emotions["neutral"]
		sadness = emotions["sadness"]
		surprise = emotions["surprise"]
		#takes prevailing emotion from image
		emotion = max([anger, contempt, disgust, fear, happiness,
					   neutral, sadness, surprise])
		#returns one of four emotions based on emotions in datafile used for 
		#machine learning 
		if (emotion == anger or emotion == contempt or  emotion == disgust):
			return "angry"
		elif (emotion == fear or emotion == sadness):
			return "sad"
		elif (emotion == neutral):
			return "relaxed"
		else:
			return "happy"
	else:
		return "happy"
