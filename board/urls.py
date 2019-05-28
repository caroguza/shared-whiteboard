from django.urls import path
from board.views import IndexView, BoardView

from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('board/', BoardView.as_view(), name='board'),
]