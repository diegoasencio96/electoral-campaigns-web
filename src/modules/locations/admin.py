from django.contrib import admin
from .models import Country, Region, City, Zone, Neighborhood, VotingPost


# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alfa_two', 'alfa_three', 'phone_code', 'icon')
    search_fields = ('name', 'alfa_two', 'alfa_three')
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'alfa_two', 'alfa_three', 'phone_code', 'icon')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo país'),
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country', )
    search_fields = ('name', 'country__name')
    autocomplete_fields = ['country']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'country')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo departamento'),
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state', )
    search_fields = ('name', 'state__name')
    autocomplete_fields = ['state']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'state')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo municipio'),
    )


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    autocomplete_fields = ['city']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'city')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo tipo de zona'),
    )


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone_type')
    search_fields = ('name', 'zone_type__name')
    list_filter = ('zone_type',)
    autocomplete_fields = ['zone_type']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'zone_type')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo tipo de zona'),
    )


@admin.register(VotingPost)
class VotingPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector')
    search_fields = ('name', 'sector__name')
    list_filter = ('sector',)
    autocomplete_fields = ['sector']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'sector')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo puesto de votación'),
    )
