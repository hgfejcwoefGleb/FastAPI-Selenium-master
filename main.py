from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    action = req.get('request', {}).get('command')

    if action == 'привет':
        response_text = 'Привет! Как я могу помочь?'
    elif action == 'пока':
        response_text = 'Пока! Возвращайтесь еще!'
    else:
        response_text = 'Извините, я не понял ваш запрос.'

    response = {
        'response': {
            'text': response_text,
            'end_session': False
        },
        'version': req['version']
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
