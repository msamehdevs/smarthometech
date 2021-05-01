from django.db import models

# Create your models here.

class Board(models.Model):
    board = models.CharField(max_length=200)
    last_request = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.board

class Output(models.Model):
    name = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    gpio = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name
