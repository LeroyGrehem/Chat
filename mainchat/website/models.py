from django.db import models

# Create your models here.
class Users(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return ({self.user_name})



