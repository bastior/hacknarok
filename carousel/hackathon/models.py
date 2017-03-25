from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class LinkedinProfile(models.Model):
    user = models.ForeignKey(User)
    linkedin_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    fb_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)


class Recruiter(models.Model):
    name = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')
    company_name = models.CharField(max_length=100, default='')
    user_profile = models.OneToOneField(UserProfile)


class Technology(models.Model):
    expertise = models.IntegerField()
    name = models.CharField(max_length=100, default='PHP')


class Offer(models.Model):
    lower_cash = models.IntegerField()
    higher_cash = models.IntegerField()
    location = models.CharField(max_length=100, default='')
    recruiter = models.ForeignKey(Recruiter, default=0)
    employment_type = models.CharField(max_length=100, default='')
    remote_work = models.CharField(max_length=100, default='')
    technologies = models.ManyToManyField(Technology)
    sports_card = models.BooleanField(default=False)
    private_medical_care = models.BooleanField(default=False)
    project_description = models.CharField(max_length=3000, default='')


class Recruit(models.Model):
    name = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')
    expected_lower_cash = models.CharField(max_length=100, default='')
    expected_higher_cash = models.CharField(max_length=100, default='')
    expected_location = models.CharField(max_length=100, default='')
    expected_secondary_location = models.CharField(max_length=100, default='')
    technologies = models.ManyToManyField(Technology)
    user_profile = models.OneToOneField(UserProfile)
    accepted_offers = models.ManyToManyField(Offer, related_name='accepted_offers')
    declined_offers = models.ManyToManyField(Offer, related_name='declined_offers')
