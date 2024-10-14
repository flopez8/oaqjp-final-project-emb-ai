import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = jsonObj, headers=header)  

    jsonResponse = json.loads(response.text)

    if response.status_code == 400:
        return {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None',
            'dominant_emotion': 'None'
        }

    emotions = jsonResponse['emotionPredictions'][0]['emotion']


    greater_value = max(emotions.values())
    
    dominant_emotion = [key for key, value in emotions.items() if value == greater_value][0]
    
    formatted_response = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
        }
    
    return formatted_response  