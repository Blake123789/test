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

LINE_CHANNEL_ACCESS_TOKEN = 'ZGkii5Rne/0kW0YRRg0beQnC8vo+Mp77c+MR0rkWWSqO8ViYIa3s2sPoCkELfeMSbcG8KbZY48appOR/N4scUNwZhQTh3yQsTvNPOY24yKFTwMpCe3A6usVLHjwHcLHjz6PcMNo//ii25VyzMqL86AdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '26a45336776c500fc75e6e6b151124c7'
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(msg))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)