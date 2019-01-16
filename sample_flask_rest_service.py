#!flask/bin/python
# from flask import Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/s2t' , methods=['POST'] )
def accountXML():
    _url = request.json.get('url')
    print(_url)

    from s2t import processAudio, download
    download(_url)
    transcript = processAudio()

    # transcript = 'none'
    print (transcript)
    return jsonify({'text': transcript})

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0')
