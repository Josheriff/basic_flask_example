from flask import Flask, request, jsonify
from persistence import update_from_front

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def hello_world():
         
    if request.method == 'POST':
        data = request.json
        update_from_front(data)



if __name__ == "__main__":
    app.run()