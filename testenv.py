from flask import Flask, request, render_template, redirect

app = Flask(__name__)  # ✅ Fixed

# In-memory student data
students = {}

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/students', methods=['POST'])
def add_student():
    student_id = request.form.get('id')
    name = request.form.get('name')

    if student_id in students:
        return "Student already exists", 400

    students[student_id] = {"name": name}
    return redirect('/')

@app.route('/students/update/<student_id>', methods=['POST'])
def update_student(student_id):
    if student_id not in students:
        return "Student not found", 404

    new_name = request.form.get('name')
    students[student_id]['name'] = new_name
    return redirect('/')

@app.route('/students/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    if student_id in students:
        students.pop(student_id)
    return redirect('/')

if __name__ == '__main__':  # ✅ Fixed
    app.run(debug=True, host='0.0.0.0', port=5000)
