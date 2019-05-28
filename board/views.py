from django.views.generic import View
from django.shortcuts import render
from board.models import Board

class IndexView(View):
    def get(self, request):
        return render(request, 'board/index.html', {})


class BoardView(View):
    def post(self, request):
        username = request.POST['username']
        previous_coordinates = Board.objects.values('coordinate_x', 'coordinate_y', 'prevx', 'prevy', 'is_point').filter(username=username)
        context = {
            'username': username,
            'previous_coordinates': previous_coordinates
        }
        return render(request, 'board/board.html', context)
