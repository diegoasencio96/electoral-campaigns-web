from django.contrib import admin
from .models import PoliticalParty
# Register your models here.


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        #if getattr(obj, 'campaign', None) is None:
        #    obj.campaign = request.user.campaign
        obj.save()

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset #.filter(campaign=request.user.campaign)

