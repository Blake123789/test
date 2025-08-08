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

LINE_CHANNEL_ACCESS_TOKEN = 'U9cqG5qr7Wm2jbrnoubgQ8dMSZGh6Tokqg0TB+Aapu7QM68gLYu2P0uumAecfIBSqPzdJ/xNO/W2H9QFM5ZLfOa5tDQ05y2hvn3FsJxYUXXynUa4Xx5dsLdGWFiyuvB5AQwa8vVTo2cmAJp962Y9CgdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = 'c80a27210d45f487458681b9402ebabc'
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