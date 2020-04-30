from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'seeker', 'job_title', 'location', 'skills', 'links', 'availability']
    search_fields = ['job_title', 'location']
    list_filter = ['job_title', 'location', 'availability']


admin.site.register(Listing, ListingAdmin)
