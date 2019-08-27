from django.contrib import admin
from .models import Meeting, ListPeople, Person, TypeMeeting, CampaignCharge, Campaign
from django_mptt_admin.admin import DjangoMpttAdmin
from import_export.admin import ImportExportModelAdmin
from .forms import MeetingForm


# Register your models here.


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    # resource_class = PersonResource
    # form = PersonForm
    list_display = ('first_name', 'last_name', 'sex', 'identification_card', 'cellphone', 'email', 'is_voter',
                    'campaign_charge', 'parent')
    list_filter = ('sex', 'is_voter', 'country', 'state', 'city', 'zone', 'sector', 'voting_post', )
    # raw_id_fields = ('assistant', )
    suit_list_filter_horizontal = ('campaign_charge', 'parent')
    search_fields = ('first_name', 'last_name', 'identification_card', 'cellphone', 'email', 'address')
    autocomplete_fields = ['campaign_charge', 'parent', 'country', 'state', 'city', 'zone', 'sector', 'voting_post']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('first_name', 'last_name', 'sex', 'year_old', 'identification_card', 'is_voter',
                       'campaign_charge', 'parent')
        }),
        (None, {
            'classes': ('suit-tab suit-tab-contact-data',),
            'fields': ('cellphone', 'email',)
        }),
        (None, {
            'classes': ('suit-tab suit-tab-ubication',),
            'fields': ('country', 'state', 'city', 'zone', 'sector', 'address')
        }),
        (None, {
            'classes': ('suit-tab suit-tab-voting-data',),
            'fields': ('voting_post', )
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
        ('contact-data', 'Datos de contacto'),
        ('ubication', 'Datos de ubicación'),
        ('voting-data', 'Datos de votación'),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'campaign', None) is None:
            obj.campaign = request.user.campaign
        obj.save()

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(campaign=request.user.campaign)


class SurveyedInline(admin.TabularInline):
    model = Person.list_people.through
    extra = 1
    suit_classes = 'suit-tab suit-tab-list'
    autocomplete_fields = ['person', 'meeting']


@admin.register(Meeting)
class MeetingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = MeetingForm
    list_display = ('id', 'candidature', 'date', 'start_time', 'end_time')
    list_filter = ('type_activity',)
    search_fields = ('name', 'type_activity__name', 'candidature__name', 'date')
    autocomplete_fields = ['type_activity', 'country', 'state', 'city', 'zone', 'sector']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('date', 'start_time', 'end_time', 'type_activity', 'country', \
                       'state', 'city', 'zone', 'sector', 'address','number_chairs', 'number_tables', \
                       'number_snacks', 'number_gifts', 'observations',)
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
    )

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(candidature=request.user.campaign)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'candidature', None) is None:
            obj.candidature = request.user.campaign
        obj.save()


@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'number', 'political_party')
    search_fields = ('name', 'number', 'political_party__name')
    autocomplete_fields = ['political_party']

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(id=request.user.campaign)


@admin.register(CampaignCharge)
class CampaignChargeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', 'campaign', 'parent__name')
    exclude = ('campaign', )
    autocomplete_fields = ['parent']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'campaign', None) is None:
            obj.campaign = request.user.campaign
        obj.save()

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(campaign=request.user.campaign)


@admin.register(TypeMeeting)
class TypeMeetignAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'campaign',)
    exclude = ('campaign', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'campaign', None) is None:
            obj.campaign = request.user.campaign
        obj.save()

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(campaign=request.user.campaign)


@admin.register(ListPeople)
class ListPeopleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_list', 'date', 'country', 'state', 'city', 'ubication')
    search_fields = ('id_list', 'date', 'country__name', 'state__name', 'city__name', 'ubication')
    exclude = ('campaign', )
    autocomplete_fields = ['country', 'state', 'city']
    inlines = [SurveyedInline]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                'id_list', 'date', 'country', 'state', 'city', 'ubication')
        }),
    )

    suit_form_tabs = (
        ('general', 'Planilla'),
        ('list', 'Listado de personas'),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'campaign', None) is None:
            obj.campaign = request.user.campaign
        obj.save()

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(campaign=request.user.campaign)
