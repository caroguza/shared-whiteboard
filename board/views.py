from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from board.models import Stroke


class IndexView(View):
    def get(self, request):
        return render(request, 'board/index.html', {})


class BoardView(View):
    def get(self, request):
        username = request.GET['username']
        previous_strokes = Stroke.get_user_strokes(username)
        context = {
            'username': username,
            'previous_strokes': previous_strokes
        }

        return render(request, 'board/board.html', context)


class ExportDraw(View):
    def get(self, request, username):
        user_strokes = Stroke.get_user_strokes(username=username)
        file_name = f'{username}_strokes.json'
        json_file = JsonResponse({username: list(user_strokes)})
        response = HttpResponse(json_file)
        response['content_type'] = 'application/json'
        response['Content-Disposition'] = f'attachment;filename={file_name}'

        return response

