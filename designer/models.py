from django.db import models

class RoomLayout(models.Model):
    name = models.CharField(max_length=100, default="My Scandinavian Studio")
    wall_color = models.CharField(max_length=20, default="0xfaf9f6")
    floor_color = models.CharField(max_length=20, default="0xe3d3c3")
    furniture_data = models.JSONField(default=list)  # Stores types and positions of spawned items
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"