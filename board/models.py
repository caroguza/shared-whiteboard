from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)


class Stroke(models.Model):
    username = models.CharField(max_length=225)
    timestamp = models.DateTimeField(auto_now_add=True)
    prev_x = models.IntegerField(null=True)
    prev_y = models.IntegerField(null=True)
    coordenate_x = models.IntegerField()
    coordenate_y = models.IntegerField()
    is_point = models.IntegerField(default=0)
    color = models.CharField(max_length=225, default='black')

    onscreen = models.BooleanField(default=True)

    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

    @classmethod
    def get_user_strokes(cls, username):
        strokes = cls.objects.filter(
            username=username,
            onscreen=True,
        ).values(
            'coordenate_x', 
            'coordenate_y', 
            'prev_x', 
            'prev_y', 
            'is_point', 
            'color'
        )
                                        
        return strokes
