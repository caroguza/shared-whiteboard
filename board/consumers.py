import json

from channels.generic.websocket import WebsocketConsumer

from board.models import Stroke, Image


class BoardConsumer(WebsocketConsumer):
    def connect(self):
        self.board_group_name = 'board'
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
            self.save_coordinates(username, coordenates, color)
        elif action == 'save':
            image_name = text_data_json['image_name']
            self.save_image(username, image_name)
        elif action == 'load':
            image_name = text_data_json['image_name']
            self.load_image(username, image_name)

    def save_image(self, username, image_name):
        image = Image.objects.create(name=image_name)
        image.save()
        print(f'saved image with name {image_name}')
        Stroke.objects.filter(onscreen=True).update(image=image)

    def load_image(self, username, image_name):
        self.clear_board(username)
        image = Image.objects.get(name=image_name)
        strokes = Stroke.objects.filter(image=image)
        strokes.update(onscreen=True)
        print(f'loading image with name {image_name}')
        self.send_strokes(strokes)

    def save_coordinates(self, username, coordinates, color):
        for coordinate in coordinates:
            Stroke.objects.create(
                username=username, 
                prev_x=coordinate['prevX'], 
                prev_y=coordinate['prevY'], 
                coordenate_x=coordinate['x'],
                coordenate_y=coordinate['y'], 
                is_point=coordinate['is_point'], 
                color=color
            )
                
    def clear_board(self, username):
        strokes = Stroke.objects.filter(username=username)
        strokes.update(onscreen=False)

    def send_strokes(self, strokes):
        message = json.dumps({
            'strokes': [
                {
                    'prev_x': stroke.prev_x,
                    'prev_y': stroke.prev_y,
                    'coordenate_x': stroke.coordenate_x,
                    'coordenate_y': stroke.coordenate_y,
                    'is_point': stroke.is_point,
                    'color': stroke.color,
                }
                for stroke in strokes
            ]
        })
        self.send(message)
