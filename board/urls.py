from django.urls import path
from board.views import IndexView, BoardView, ExportDraw

from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('board/', BoardView.as_view(), name='board'),
    path('export/<username>', ExportDraw.as_view(), name='export'),
]