from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            form_data = request.json

            if form_data is None:
                raise ValueError("No JSON data found in the request body.")

            # Save form data to a JSON file
            with open('form_data.json', 'a') as json_file:
                json.dump(form_data, json_file)
                json_file.write('\n')

            response_data = {"message": "Form data received and saved to JSON file successfully"}
        except Exception as e:
            response_data = {"error": str(e)}

        response = jsonify(response_data)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')  # Allow requests from your frontend
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')  # Allow specific methods
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')  # Allow specific headers

        return response

if __name__ == '__main__':
    app.run(debug=True)
