from flask import Flask, render_template, request, jsonify, session
from algorythms.finding_polynom import *
from algorythms.securing_messege import *
from algorythms.binary_to_algeb import *
from algorythms.controling_message import *
from algorythms.find_error import *
from algorythms.find_error import *

app = Flask(__name__)
app.secret_key = "123456789"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/first_post', methods=['POST', 'GET'])
def first_post():
    if request.method == "POST":
        data = request.get_json()

        message = [int(i) for i in data[0]]
        session["message"] = message

        nk = data[1].split(",")
        
        n = int(nk[0])
        session["n"] = n

        k = int(nk[1])
        session["k"] = k

        polynoms = find_polynoms(n,k)
        session["polynoms"] = polynoms

    return jsonify(polynoms)

@app.route('/second_post', methods=['POST', 'GET'])
def second_post():
    if request.method == "POST":
        choice = int(request.get_json())

        n = session["n"] 
        k = session["k"]
        message = session["message"]
        polynoms = session["polynoms"]

        polynom = polynoms[choice]

        data = sequre_polynom(message, polynom, n, k)

    return jsonify(data)

@app.route('/third_post', methods=['POST', 'GET'])
def third_post():
    if request.method == "POST":
        data = request.get_json()
        message = [int(i) for i in data[0]]
        gen_polynom = [int(i) for i in data[1]]

        result = []
        result.append(binary_to_algeb(message))
        #is error and where

        correct = control_message(message, gen_polynom)
        if type(correct) is bool:
            result.append(correct)
        else:
            error = find_error(message, gen_polynom, correct[1])
            print(error)
            correct_message_bin = repair_message(message, error)
            error = binary_to_algeb(error)
            print(correct_message_bin)
            correct_message_alg = binary_to_algeb(correct_message_bin)
            print(correct_message_alg)

            result.append(correct[0])
            result.append([error, correct_message_bin, correct_message_alg])
        print(result)
            
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)