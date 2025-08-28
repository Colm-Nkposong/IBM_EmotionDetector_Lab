import requests, json # Import Requests to handle HTTP Requests, Json handles the response objects

def emotion_detecter(text_to_analyze):
    '''A simple Sentiment analyzer utilizing the IBM Watson Lib'''
    # Uses a BERT based Sentiment Analysis function of the embedded IBM Watson NLP Library

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }
    # URL, headers, and the input json format required to accesses the Emotion Predict function from the Watson NLP Lib

    if not text_to_analyze:
        # Will return Invalid Input if the input is left blank
        return {'anger' : None,
        'disgust' : None,
        'fear' : None,
        'joy' : None,
        'sadness' : None,
        'dominant_emotion' : None}

    # Send a post request using the above inputs
    response = requests.post(url, json = json_obj, headers = headers)
    
    formatted_response = json.loads(response.text)
    # Format the resonse into a parsable json object 

    # Return values as none if the server recieves a 500 error caused by invalid text
    if response.status_code == 500 or response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # If the input text is valid, obtain it from the dictionary
    elif response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        base_score = 0
        for val in formatted_response['emotionPredictions'][0]['emotion']:
            if formatted_response['emotionPredictions'][0]['emotion'][val] >= base_score:
                dominant_emotion = val
                base_score = formatted_response['emotionPredictions'][0]['emotion'][val]

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}
