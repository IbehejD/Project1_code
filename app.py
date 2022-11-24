from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/first_post', methods=['POST', 'GET'])
def first_post():
    if request.method == "POST":
        data = int(request.get_json())
 
    results = [i for i in range(1, data + 1)]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True)