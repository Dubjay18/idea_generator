import os

from utils.preprocessing import Preprocessing
from utils.idea_generator import Generator
from utils.miro_integration import MiroIntegrator

from flask import Flask, request, jsonify, redirect


app = Flask(__name__)
app.env = 'development'

@app.route('/miro_plugin', methods=['GET'])
def home():
    # @TODO: add the miro_plugin.html
    pass

@app.route('/miro_plugin/generate_ideas', methods=['POST'])
def generate_ideas():
    raw_question = request.form['question']
    # @TODO: preprocessing and then generate ideas
    # @TODO: add the answers to sticker and then send it to miro
    pass
