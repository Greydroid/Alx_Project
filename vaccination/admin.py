from django.contrib import admin
from .models import Vaccination

admin.site.register(Vaccination)


from django.contrib import admin

# Custom admin branding
admin.site.site_header = "VetTrack"
admin.site.site_title = "Animal Vaccination Tracker"
admin.site.index_title = "Welcome to VetTrack – Your world's best Pet and Animal Vaccination Tracker"

