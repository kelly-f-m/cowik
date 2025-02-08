from flask import Flask
import tibiadata

app = Flask(__name__)

@app.route('/')
def hello():
    return "Service is running! (●'◡'●)"

@app.route('/charinfo/<string:name>', methods=['GET'])
def character_info(name):
    data = tibiadata.get_character_info(name)
    return data

if __name__ == "__main__": 
    app.run(debug=True)