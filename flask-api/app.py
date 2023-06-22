import os
from flask import Flask, request, jsonify
from bardapi import Bard
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Get the API key from the environment variable
api_key = 'XQimvVD1RUeYIhVVJKDM-oilymZHrWdzXIuwZjiTdcxuwYFZ1qNgE7MDBvgMwrEykrp0XQ.'


def get_answer(prompt):
    prompt1 = "You are a professional Chatbot integrated into ONE Technology Services' website and social media platforms. Your purpose is to provide information about the company's software services. Users can contact the company on LinkedIn (https://www.linkedin.com/company/one-technology-services/) and Twitter (https://twitter.com/ONETechnologySer). Please provide a response to the following question related to the services of ONE Technology Services:"

    try:
        # Use Bard to get an answer to the prompt
        answer = Bard(api_key).get_answer(prompt1 + prompt)['content']
        return answer
    except Exception as e:
        return str(e)


@app.route('/create-response/<prompt>', methods=['GET'])
def create_response(prompt):
    # Log the prompt in the terminal
    print(prompt)

    # Get the answer using the get_answer function
    answer = get_answer(prompt)
    response = jsonify(response=answer)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
