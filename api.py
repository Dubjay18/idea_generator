import os
import json

from flask import Flask, request, jsonify


from utils.preprocessing import Preprocessing
from utils.idea_generator import Generator


app = Flask(__name__)
app.env = 'development'

@app.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome Idea Generator!'})

@app.route('/api/idea_generator', methods=['GET'])
def get_idea():
    if(os.path.isfile("./data/body.json")):
        with open("./data/body.json", "r") as read_file:
            body = json.load(read_file)
            return jsonify(body), 200
    else:
        return jsonify({'message': 'No body file not exist!'}),400
    

@app.route('/api/idea_generator', methods=['POST'])
def create_idea():
    data = request.get_json()
    raw_question = data['question']
    quantity = data['quantity']
    isCrazy = data['isCrazy']
    workshop_method = data['workshop_method']
    
# the below try except handle also the empty input from user, so we should always have a text gpt3
# and I will implement this in the preprocessing.py file (checked with Maxim)
    try:
        prepocessing = Preprocessing(input_data=raw_question)
    except ValueError as e:
        return jsonify({"Error" : e}), 400
    else:
        if workshop_method == "hmw": prepocessing.process_hmw()
        elif workshop_method == "opposite": prepocessing.process_opposite()
        elif workshop_method == "bad idea": prepocessing.process_bad_idea()
        elif workshop_method == "free text": prepocessing.process_free_text()

    if not prepocessing.output_data:
        prepered_question = f'Suggest 10 ideas for "{raw_question}"'
    else:
        prepered_question = prepocessing.output_data
    
    generator = Generator(prepared_question=prepered_question, number_of_idea=quantity, crazy=isCrazy, workshop_method=workshop_method)
    if (generator.generate_idea()):
        if (isCrazy):
            idea_list = generator.idea_list_enhaced
            return jsonify({'idea_list': idea_list}), 200
        else:
            idea_list = generator.idea_list
            return jsonify({'idea_list': idea_list}), 200
    else:
        return jsonify({'message': 'No idea generated!'}), 400

    


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, )