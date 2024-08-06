from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    # Kirim balasan ke chat
    response_text = "Balasan dari bot: " + text
    requests.post(f'https://api.telegram.org/bot6683299629:AAHt20PuoQV8lgbrWYGGf9lzfEhleNbZHQ8/sendMessage', json={
        'chat_id': chat_id,
        'text': response_text
    })
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
