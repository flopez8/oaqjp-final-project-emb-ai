'''This is the server that runs the emotion detection page'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detector():
    '''Function used to detect the emotions in the given input'''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!."

    response_value = """For the given statement, the system response is
     '{}': {}, '{}': {}, '{}': {}, '{}': {} and '{}': {}. The dominant emotion is {}."""
    return response_value.format(
        'anger', response['anger'], 
        'disgust', response['disgust'], 
        'fear', response['fear'], 
        'joy', response['joy'], 
        'sadness', response['sadness'], 
        response['dominant_emotion'])

@app.route("/")
def render_index_page():
    '''Function to render the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
