from django.db import models


class Board(models.Model):
    username = models.CharField(max_length=225)
    timestamp = models.DateTimeField(auto_now_add=True)
    prevx = models.IntegerField(null=True)
    prevy = models.IntegerField(null=True)
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    stroke_identifier = models.IntegerField(blank=True)

    def __str__(self):
        return self.username