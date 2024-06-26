from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse

User = get_user_model()


class Response(models.Model):
    user = models.ForeignKey(User, related_name='responses', on_delete=models.SET_NULL, null=True)
    input = models.TextField(blank=True, default='', max_length=3000)
    text = models.TextField(blank=True, default='', max_length=3000)
    request = models.CharField(blank=True, default='', max_length=10)
    created_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request

    def save(self, *args, **kwargs):
        self.created_dt = timezone.now()
        # self.save()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tutor:tutor_detail', kwargs={'pk': self.id},)

    class Meta:
        ordering = ['-created_dt']
