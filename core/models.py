from django.db import models

class Waitlist(models.Model):
  email = models.EmailField(max_length=255)
  date_joined = models.DateTimeField(auto_now_add=True)

  class Meta:
      verbose_name_plural = "Waitlist"
  
  def __str__(self):
        return f'{self.email}'