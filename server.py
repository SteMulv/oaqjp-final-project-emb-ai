from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text from the web request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function to run the AI analysis and store the JSON response as response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!"

    else:
        # Format the emotion values into a string
        emotion_string = ' , '.join([f"'{emotion}': {value}" for emotion, value in response.items() if emotion != 'dominant_emotion'])

        # Extract the dominant emotion (already present in the response)
        dominant_emotion = response["dominant_emotion"]

        # Prepare the formatted response
        formatted_response = f"For the given statement, the system response is {emotion_string}. The dominant emotion is {dominant_emotion}"

        return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
