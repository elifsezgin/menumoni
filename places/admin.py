from django.contrib import admin

from places.models import (Place, Item, Media)

admin.site.register(Place)
admin.site.register(Item)
admin.site.register(Media)