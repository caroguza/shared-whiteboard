from django.db import models


class Board(models.Model):
    username = models.CharField(max_length=225)
    timestamp = models.DateTimeField(auto_now_add=True)
    prevx = models.IntegerField(null=True)
    prevy = models.IntegerField(null=True)
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    is_point = models.IntegerField(default=0)

    def __str__(self):
        return self.username