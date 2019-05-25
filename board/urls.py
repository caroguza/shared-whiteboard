from django.urls import path
from board.views import IndexView

from . import views

urlpatterns = [
    path('', IndexView.as_view()),
]