from flask import Flask, request, jsonify

app = Flask(__name__)
students = []

@app.route('/students', methods=['POST'])
def add_student():
    student_data = request.get_json()
    students.append(student_data)
    return jsonify({'message': 'Student added successfully'})

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student['student_id'] == student_id:
            return jsonify(student)
    return jsonify({'message': 'Student not found'})

if __name__ == '__main__':
    app.run()
