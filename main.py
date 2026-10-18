from flask import Flask, request, jsonify
import config

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query = req.get('queryResult', {}).get('queryText', '').lower()
    
    response_text = f"Welcome to the AI Food & Culture Guide for {config.DEFAULT_CITY}! What are you craving today?"
    
    if 'food' in query or 'eat' in query or 'restaurant' in query or 'taste' in query:
        response_text = f"Based on your taste preferences, I recommend trying the best rated {config.DEFAULT_CUISINE} spots nearby!"
    elif 'culture' in query or 'landmark' in query or 'history' in query or 'place' in query:
        response_text = "Here are the top cultural landmarks and historical spots you can explore around your current location."
    elif 'trip' in query or 'tour' in query:
        response_text = "I've combined a custom food-and-heritage trail just for you. Enjoy your exploration!"

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(port=5000, debug=config.DEBUG_MODE)
