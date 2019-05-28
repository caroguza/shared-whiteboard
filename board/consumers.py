from channels.generic.websocket import WebsocketConsumer
from board.models import Board
import json


class BoardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        coordinates = text_data_json['coordinates']
        username = text_data_json['username']
        self.send(text_data=json.dumps({
            'message': 'hola'
        }))

        self.save_coordenates(coordinates, username)

    def save_coordenates(self, coordinates, username):
        for coordinate in coordinates:
            stroke =Board(username=username, prevx=coordinate['prevX'], prevy=coordinate['prevY'], coordinate_x=coordinate['x'],
            coordinate_y=coordinate['y'], is_point=coordinate['is_point'])
            stroke.save()
        

    
