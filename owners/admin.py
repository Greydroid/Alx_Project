from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")



from django.contrib import admin

admin.site.site_header = "Vet Track Administration"
admin.site.site_title = "Vet Track Admin Portal"
admin.site.index_title = "Welcome to Vet Track"

