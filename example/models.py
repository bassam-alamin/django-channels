from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    # This bit of code will allow us to only see the 10 most recent messages

    def last_10_messages():
        return Message.objects.order_by("-timestamp").all()[:10]
