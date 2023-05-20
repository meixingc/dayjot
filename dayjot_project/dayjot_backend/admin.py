from django.contrib import admin
from .models import User, Entry, Water, Food, Exercise

admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Water)
admin.site.register(Food)
admin.site.register(Exercise)