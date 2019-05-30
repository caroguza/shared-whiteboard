from django.views.generic import View
from django.shortcuts import render

from board.models import Board


class IndexView(View):
    def get(self, request):
        return render(request, 'board/index.html', {})


class BoardView(View):
    def post(self, request):
        username = request.POST['username']
        previous_strokes = Board.get_user_strokes(username)
        context = {
            'username': username,
            'previous_strokes': previous_strokes
        }
        
        return render(request, 'board/board.html', context)
