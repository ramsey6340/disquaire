from django.contrib import admin
from listings.models import *

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed','genre', 'active', 'official_home_page')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','sold','year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
