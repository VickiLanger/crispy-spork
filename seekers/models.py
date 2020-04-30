# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone

# TODO: Allow each User to add multiple Job_Listing


# Create your models here.
class Listing(models.Model):
    # listing_id = models.BigAutoField()
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    links = models.URLField(max_length=200)  # projects, blog, whatevs
    availability = models.DateField(auto_now=False, auto_now_add=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.job_title


class Skill():
    pass


class Job_Title():
    pass
