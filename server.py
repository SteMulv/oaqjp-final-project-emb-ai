"""
This is the server for the emotion detection application.
It provides an API endpoint that accepts a text input and returns the emotional analysis
with a dominant emotion prediction.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Handle emotion detection requests by analyzing the provided text 
    and returning the emotion values and dominant emotion.
    """
    # Retrieve the text from the web request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function to run the AI analysis and store the JSON response
    response = emotion_detector(text_to_analyze)

    # Check if the response contains a valid dominant emotion
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Format the emotion values into a string (excluding 'dominant_emotion' from the list)
    emotion_string = ', '.join(
        [f"'{emotion}': {value}"
        for emotion, value in response.items()
        if emotion != 'dominant_emotion']
)

    # Extract the dominant emotion (already present in the response)
    dominant_emotion = response["dominant_emotion"]

    # Prepare the formatted response
    formatted_response = (
        f"For the given statement, the system response is {emotion_string}. "
        f"The dominant emotion is {dominant_emotion}"
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000, debug=True)
