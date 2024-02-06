from flask import Flask, request, jsonify
from telegram import Bot


app = Flask(__name__)
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
telegram_chat_id = "YOUR_TELEGRAM_CHAT_ID"

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = request.json
    if 'push' in data['event']:
        repo_name = data['repository']['full_name']
        commits = data['commits']
        for commit in commits:
            author = commit['author']['name']
            message = commit['message']
            send_telegram_message(f"Repo: {repo_name}\nAuthor: {author}\nMessage: {message}")
    return jsonify({'message': 'Received'}), 200

def send_telegram_message(message):
    bot = Bot(token=telegram_bot_token)
    bot.send_message(chat_id=telegram_chat_id, text=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
