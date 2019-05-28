from django.views.generic import View
from django.shortcuts import render
from board.models import Board

class IndexView(View):
    def get(self, request):
        previous_coordinates = Board.objects.values('coordinate_x', 'coordinate_y', 'prevx', 'prevy', 'is_point').filter(username='user4')
        context = {
            'previous_coordinates': previous_coordinates
        }

        return render(request, 'board/index.html', context)


