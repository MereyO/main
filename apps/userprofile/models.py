from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# from apps.common.forms import User



class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    INTERESTING_CHOICES = (
        ('Programming', 'Programming'),
        ('Business training', 'Business training'),
        ('Computer games', 'Computer games'),
        ('Music', 'Music'),
        ('Creation', 'Creation'),
        ('Sport', 'Sport'),
        ('Reading', 'Reading'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usernickname = models.CharField(max_length=500, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.CharField(choices=INTERESTING_CHOICES, max_length=60, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7, null=True, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    # profile_image = models.ImageField()



    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()