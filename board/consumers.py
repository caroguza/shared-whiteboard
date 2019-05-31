import json

from channels.generic.websocket import WebsocketConsumer

from board.models import Stroke


class BoardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        action = text_data_json['action']
        username = text_data_json['username']
        
        if action == 'clear':
            self.clear_board(username)
        elif action == 'draw':
            coordenates = text_data_json['coordenates']
            color = text_data_json['color']
            self.save_coordenates(username, coordenates, color)


    def save_coordenates(self, username, coordenates, color):
        for coordenate in coordenates:
            Stroke.objects.create(
                username=username, 
                prev_x=coordenate['prevX'], 
                prev_y=coordenate['prevY'], 
                coordenate_x=coordenate['x'],
                coordenate_y=coordenate['y'], 
                is_point=coordenate['is_point'], 
                color=color
            )
                
    def clear_board(self, username):
        Stroke.objects.filter(username=username).delete()
