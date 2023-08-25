from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient 
import json

app = Flask(__name__)
CORS(app)


client = MongoClient('mongodb+srv://Jaimishra20031:Jai31072003@jaicluster.xau2qru.mongodb.net/?retryWrites=true&w=majority')  
db = client['form_data'] 
collection = db['submissions']  

@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        form_data = request.json

        collection.insert_one(form_data)

        response_data = {"message": "Form data received and saved successfully"}
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
