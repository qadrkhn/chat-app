from django.db import models

class Message(models.Model):
    sender = models.ForeignKey('accounts.Account', on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey('accounts.Account', on_delete=models.PROTECT, related_name='receiver')

    content = models.TextField()

    time_sent = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.sender.email} -> {self.receiver.email}'
