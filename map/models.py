from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

class Event(models.Model):
    EVERYONE = 1
    EDITORS = 2
    CREATOR = 3
    PUBLIC = 1
    LINK = 2
    PRIVATE = 3
    EDIT_STATUS = (
        (EVERYONE, 'Everyone can edit'),
        (EDITORS, 'Editors can edit'),
        (CREATOR, 'Just creator can edit')
    )
    SHARE_STATUS = (
        (PUBLIC, 'everyone can see'),
        (LINK, 'anyone with link'),
        (PRIVATE, 'only specific users'),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    tags = models.ManyToManyField(Tag)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name="created_events")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    share_status = models.SmallIntegerField(choices=SHARE_STATUS, default=PUBLIC, verbose_name="share status")
    share_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name="share with", related_name="shared_events")
    edit_status = models.SmallIntegerField(choices=EDIT_STATUS, default=CREATOR, verbose_name="edit status")
    edit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name="editors", related_name="events_editor")

    def __str__(self):
        return self.title


class Place(models.Model):
    EVERYONE = 1
    EDITORS = 2
    CREATOR = 3
    PUBLIC = 1
    LINK = 2
    PRIVATE = 3
    EDIT_STATUS = (
        (EVERYONE, 'Everyone can edit'),
        (EDITORS, 'Editors can edit'),
        (CREATOR, 'Just creator can edit')
    )
    SHARE_STATUS = (
        (PUBLIC, 'everyone can see'),
        (LINK, 'anyone with link'),
        (PRIVATE, 'only specific users'),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    tags = models.ManyToManyField(Tag)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name="created_places")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    share_status = models.SmallIntegerField(choices=SHARE_STATUS, default=PUBLIC, verbose_name="share status")
    share_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name="share with", related_name="shared_places")
    edit_status = models.SmallIntegerField(choices=EDIT_STATUS, default=CREATOR, verbose_name="edit status")
    edit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name="editors", related_name="places_editor")


    def __str__(self):
        return self.title


class Profile(models.Model):
    PUBLIC = 1
    LINK = 2
    PRIVATE = 3
    SHARE_STATUS = (
        (PUBLIC, 'everyone can see'),
        (LINK, 'anyone with link'),
        (PRIVATE, 'only specific users'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    avatar = models.ImageField()
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    share_status = models.SmallIntegerField(choices=SHARE_STATUS, default=PUBLIC, verbose_name="share status")
    share_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name="share with", related_name="shared_positions")

    def __str__(self):
        return f"{self.user.username} - {self.created_at:%Y-%m-%d - %H:%M}"
