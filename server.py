from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_api():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    dominant_emotion = response['dominant_emotion']
    
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="localhost", port=5000)