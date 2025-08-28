''' Executing this function initiates the execution of the emotion
    detection application via Flask channel on localhost:5000.
'''
# Import Flask, render_template, request from the flask web framework package
from flask import Flask, render_template, request

# Import the emotion_detecter function from the EmotionDetection Package
from EmotionDetection.emotion_detection import emotion_detecter

app = Flask("Emotion Detection app")

@app.route('/emotionDetector')
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        filters out the detected emotions using emotion_detecter()
        function. The output returned shows the emotional labels and their  
        score for the provided text.
    '''

    # analyze the data recieved from the interface
    text_to_analyze = request.args.get('textToAnalyze')

    output = emotion_detecter(text_to_analyze)

    anger = output['anger']
    disgust = output['disgust']
    fear = output['fear']
    joy = output['joy']
    sadness = output['sadness']
    dominant_emotion = output['dominant_emotion']

    # If our label is None due to invalid text input, return an error message
    if anger is None:
        return 'Invalid input! Please try again.'

    # Otherwise return our formatted data
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust},'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness} The dominant emotion is {dominant_emotion}."

@app.route('/')
def render_index_page():
    ''' This function renders main application
        page via the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)