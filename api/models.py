import re
from django.db import models
from django.utils.text import slugify


# Create your models here.
def convert_ytframe(url):
    video_id = url.split("watch?v=")
    print(video_id)
    return video_id[1]


class Phase(models.Model):
    def get_image_filename(instance, filename):
        title = instance.name
        slug = slugify(title)
        return "layout_image/%s-%s" % (slug, filename)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    videoView = models.CharField(max_length=100)
    videoNearby = models.CharField(max_length=100)
    videoHealth = models.CharField(max_length=100, blank=True)
    location = models.URLField(max_length=100)
    layoutImage = models.ImageField(upload_to=get_image_filename, verbose_name="Image")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.videoView) > 20:
            self.videoView = convert_ytframe(self.videoView)
        if len(self.videoNearby) > 20:
            self.videoNearby = convert_ytframe(self.videoNearby)
        if len(self.videoHealth) > 20:
            self.videoHealth = convert_ytframe(self.videoHealth)
        super(Phase, self).save(*args, **kwargs)


class PhaseImage(models.Model):
    def get_image_filename(instance, filename):
        title = instance.phase.name
        slug = slugify(title)
        return "phase_images/%s/%s" % (slug, filename)

    phase = models.ForeignKey(
        Phase, default=None, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=get_image_filename, verbose_name="Image")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phase.name


class Lock(models.Model):
    phase = models.ForeignKey(
        Phase, default=None, related_name="phase_lock", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    monthly = models.FloatField()
    area = models.FloatField()
    videoView = models.CharField(max_length=100)
    videoNearby = models.CharField(max_length=100)
    location = models.URLField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.videoView) > 20:
            self.videoView = convert_ytframe(self.videoView)
        if len(self.videoNearby) > 20:
            self.videoNearby = convert_ytframe(self.videoNearby)
        super(Lock, self).save(*args, **kwargs)


class LockImage(models.Model):
    def get_image_filename(instance, filename):
        title = instance.lock.name
        slug = slugify(title)
        return "lock_images/%s/%s" % (slug, filename)

    lock = models.ForeignKey(
        Lock, default=None, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=get_image_filename, verbose_name="Image")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lock.name


class Nearyby(models.Model):
    lock = models.ForeignKey(
        Lock, default=None, related_name="nearbies", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    distance = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.name
