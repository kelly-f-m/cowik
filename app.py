from flask import Flask
import tibiadata
import utils

app = Flask(__name__)

@app.route('/')
def hello():
    return "Service is running! (●'◡'●)"

@app.route('/charinfo/<string:name>', methods=['GET'])
def character_info(name):
    data = tibiadata.get_character_info(name)
    return data

@app.route('/guildinfo/<string:name>', methods=['GET'])
def guild_info(name):
    data = tibiadata.get_guild_info(name)
    

@app.route('/rashid', methods=['GET'])
def rashid():
    result = utils.rashid()
    return result

if __name__ == "__main__": 
    app.run(debug=True)
