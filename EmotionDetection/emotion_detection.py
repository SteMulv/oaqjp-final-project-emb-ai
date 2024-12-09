import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion by getting the key with the highest value
        dominant_emotion = max(emotion_data, key=emotion_data.get)
        
        # Create the desired output format
        output = {
            'anger': emotion_data['anger'],
            'disgust': emotion_data['disgust'],
            'fear': emotion_data['fear'],
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
            'dominant_emotion': dominant_emotion
            }
    
    elif response.status_code == 400:
        # Create the none output format
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    
    # Return the formated response
    return output
    