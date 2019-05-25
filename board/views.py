from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        context = {
            'room_name_json': 'room1'
        }
        return render(request, 'board/index.html', context)


