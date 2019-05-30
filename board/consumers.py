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
        
        action = text_data_json['action']
        username = text_data_json['username']
        self.send(text_data=json.dumps({
            'message': 'hola'
        }))

        if action == 'clear':
            self.clear_board(username)
        elif action == 'save':
            self.save_draw(username)
        else:
            coordinates = text_data_json['coordinates']
            color = text_data_json['color']
            self.save_coordenates(username, coordinates, color)

    def save_draw(self, username):
        user_draw = Board.objects.filter(username=username)\
                                 .values('prevx', 'prevy', 'coordinate_x', 'coordinate_y', 'color')

    def save_coordenates(self, username, coordinates, color):
        for coordinate in coordinates:
            stroke = Board(
                username=username, 
                prevx=coordinate['prevX'], 
                prevy=coordinate['prevY'], 
                coordinate_x=coordinate['x'],
                coordinate_y=coordinate['y'], 
                is_point=coordinate['is_point'], 
                color=color
            )
            stroke.save()

    def clear_board(self, username):
        Board.objects.filter(username=username).delete()
