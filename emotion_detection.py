import requests, json # Import Requests to handle HTTP Requests, Json handles the response objects

def emotion_detecter(text_to_analyze):
    '''A simple Sentiment analyzer utilizing the IBM Watson Lib'''
    # Uses a BERT based Sentiment Analysis function of the embedded IBM Watson NLP Library

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }
    # URL, headers, and the input json format required to accesses the Emotion Predict function from the Watson NLP Lib
    
    # Send a post request using the above inputs
    response = requests.post(url, json = json_obj, headers = headers)
    
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        
    elif response.status_code == 500:
        label = None
        score = None
        
    return {"Label": label, "Score" : score}
