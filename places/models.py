from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text

class Media(models.Model):
    image = models.ImageField(upload_to="static/images", default=None)

    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return smart_text(self.image.url)

class Place(models.Model):
    # user = models.ForeignKey(
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    coordinates = models.CharField(max_length=255, null=True, blank=False)
    telephone = models.CharField(max_length=13, blank=True, null=True)
    menu = models.ForeignKey(Media, null=True, blank=False)

    def __str__(self):
        return smart_text(self.name)



class Item(models.Model):
    #user
    place = models.ForeignKey(Place)
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    currency = models.IntegerField(default=1,
                                choices=(
                                    (1,'TRY'),
                                    (2, 'EUR'),
                                    (3, 'USD')))
    media = models.ForeignKey(Media, null=True, blank=False)
    def __str__(self):
        return smart_text(self.name)

