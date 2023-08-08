import json
import logging

import websockets

from models.message import WSMessage

from services.sender_base import SenderBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SenderWebsocket(SenderBase):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def send_message(
        self,
        ws_mess: WSMessage
    ) -> None:
        print('ws')
        # ws_server = websockets.serve(receiver, "localhost", 8765)

        uri = f'ws://{self.host}:{self.port}/'
        mess = {
            'username': ws_mess.username,
            'text': ws_mess.text,
        }
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(mess))
