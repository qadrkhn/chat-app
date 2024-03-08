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


class UserChannel(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email} -> {self.channel_name}'

    def save(self, *args, **kwargs):
        # if the user already has a channel name, then delete the old channel name
        try:
            old_channel = UserChannel.objects.get(user=self.user)
            old_channel.delete()
        except UserChannel.DoesNotExist:
            pass
        super().save(*args, **kwargs)
