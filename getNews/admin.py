from django.contrib import admin

# Register your models here.
from .models import News
from .models import Source

admin.site.register(News)
admin.site.register(Source)
