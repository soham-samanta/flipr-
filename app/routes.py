from flask import jsonify, request, abort
from app import app, db
from app.models import Note



@app.route('/notes', methods=['GET'])
def get_notes():
    # ... Implement the GET all notes functionality

@app.route('/notes', methods=['POST'])
def create_note():
    # ... Implement the POST create note functionality

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    # ... Implement the GET single note functionality

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    # ... Implement the PUT update note functionality

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    # ... Implement the DELETE note functionality
