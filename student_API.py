from operator import methodcaller
import flask
from flask import request, jsonify
import student_processor



app = flask.Flask(__name__)

app.config["DEBUG"] = True

#create data for our site
student_dictionaries = student_processor.get_student_dictionary()

#Create Routes to web pages
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Student Data API</h1>
    <p>This site makes student data avaible to you!</p>'''

#return all students
@app.route('/api/v1/resources/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)

#return students by id
@app.route('/api/v1/resources/students', methods=['GET'])
def api_id():
    #check if id is a part of the url
    #if ID is provided, assign it to a variable
    if 'id' in request.args:
        id = request.args['id']
    #if ID not provided display error in the browser
    else:
        return "Error: No id field provided. Please specify an id."
    
    #create an empty list for our results
    results = []

    #loop through dummy data and search for students dictionary with matching id
    for student in student_dictionaries:
        if id == student['id']:
            results.append(student)
            return jsonify(results)
    if(len(results) == 0):
        return f"Student with id: {id} not found"

app.run()