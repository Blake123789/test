from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import os

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = 'svcdYMNDnlmjtI9uyQwrliidwCCEaDU5qZGsYxU6i5o7NKadZ7+DPGkWs4+eX+vbhReFJi+BGQSySY9VI4WXQ9S2Pa2yjekI7hbYSZ4CqMLNRGGRmEuRncml19iEaJHp1GwaHzasVAu0AL24ZH3wnAdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '6fad9f777e3cb5d72af5cc764109628e'
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
aseurl='./static' 
audio_url = './mp3'#音樂來源

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)