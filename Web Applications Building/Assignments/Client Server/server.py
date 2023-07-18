from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = {}

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id in students:
        return jsonify(students[student_id])
    else:
        return jsonify({'error': 'Student not found'})

@app.route('/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'GET':
        return jsonify(students)
    elif request.method == 'POST':
        if request.json is not None:
            student = request.json
            students[student['student_id']] = student
            return jsonify({'message': 'Student added successfully'})
        else:
            return jsonify({'error': 'Invalid JSON payload'})

if __name__ == '__main__':
    app.run()
