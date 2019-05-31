from django.urls import path, include

urlpatterns = [
    path('', include('board.urls')),
]
