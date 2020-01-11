from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.TextField(blank=False, null=False, )
    last_name = models.TextField()
    company_name = models.CharField(max_length = 50)
    city = models.TextField()
    state = models.TextField()
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.CharField(max_length = 50)
    age = models.IntegerField()
    # owner = models.ForeignKey('auth.user', related_name='user', on_delete=models.CASCADE)
    # highlighted = modls.TextField()

    def __str__(self):
        return self.first_name