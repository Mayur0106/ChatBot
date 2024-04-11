# server.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def recycle_e_waste():
    # Logic to handle recycling e-waste
    return "Please check your local recycling center for e-waste disposal options.", ["Recycling Centers", "Donate to Charity"]

def dispose_e_waste_safely():
    # Logic to handle safe disposal of e-waste
    return "We recommend contacting local electronic recycling facilities for safe disposal.", ["Electronic Recycling Facilities", "Local Waste Management"]

def donate_e_waste():
    # Logic to handle donating e-waste
    return "Consider donating your e-waste to organizations that refurbish electronics for reuse.", ["Charities Accepting E-Waste", "Reuse Centers"]

def welcome_message():
    return "Hello! How canI help you? A]Recycle B]Dispose C]Donate ", ["Recycle", "Dispose", "Donate"]
@app.route('/dispose', methods=['POST'])
def dispose():
    data = request.json
    message = data.get('message')

    # Process the message and provide appropriate response
    if any(word in message.lower() for word in ['hi', 'hello', 'hii']):
        response, options = welcome_message()
    elif any(word in message.lower() for word in [ 'recycling', 'recycle']):
        response, options = recycle_e_waste()
    elif 'dispose' in message.lower():
        response, options = dispose_e_waste_safely()
    elif 'donate' in message.lower():
        response, options = donate_e_waste()
    else:
        response = "Sorry, I couldn't understand your request. Please try again."
        options = []
    
    return jsonify({'response': response, 'options': options})


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)
