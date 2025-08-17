"""
This is the main server file for the Emotion Detection web application.
It exposes an API endpoint to analyze text and return emotion scores.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the web application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_api():
    """
    Analyzes the text from the user and returns emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
