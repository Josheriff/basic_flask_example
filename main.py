from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        greetings = {'text':'Hello world'}
        return jsonify(greetings)
        
    if request.method == 'POST':
        data = request.json
        age = data.get('age')
        if age > 30:
            return jsonify({'text':'Esto es una app para jovenes, ve a dar de comer a las palomas'})
        return jsonify({'text':'bienvendio'})



if __name__ == "__main__":
    app.run()