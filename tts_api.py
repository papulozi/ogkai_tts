from flask import Flask, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/api/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return {"error": "Metin bulunamadı."}, 400

    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='tr')
    tts.save(filename)

    response = send_file(filename, as_attachment=True)
    os.remove(filename)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
