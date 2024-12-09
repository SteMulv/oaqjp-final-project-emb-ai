from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        emotion_values = result["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotion_values, key=emotion_values.get)
        self.assertEqual(max_emotion, "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        emotion_values = result["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotion_values, key=emotion_values.get)
        self.assertEqual(max_emotion, "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        emotion_values = result["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotion_values, key=emotion_values.get)
        self.assertEqual(max_emotion, "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        emotion_values = result["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotion_values, key=emotion_values.get)
        self.assertEqual(max_emotion, "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        emotion_values = result["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotion_values, key=emotion_values.get)
        self.assertEqual(max_emotion, "fear")

if __name__ == "__main__":
    unittest.main()
