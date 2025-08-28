from EmotionDetection.emotion_detection import emotion_detecter
import unittest

class TestEmotionDetecter(unittest.TestCase):
    def test_emotion_detecter(self):
        '''Unit tests for the emotion_detecter function'''
        #Test case for a joyful example
        result1 = emotion_detecter('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')

        #Test case for an angry example
        result2 = emotion_detecter('I am really mad about this')
        self.assertEqual(result2['dominant_emotion'], 'anger')

        #Test case for a disgusted example
        result3 = emotion_detecter('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        #Test case for a sad example
        result4 = emotion_detecter('I am so sad about this')
        self.assertEqual(result4['dominant_emotion'], 'sad')

        #Test case for a fearexample
        result5 = emotion_detecter('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_emotion'], 'fear')

# call the unit tests