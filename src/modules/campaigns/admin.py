from django.contrib import admin
from .models import Meeting, ListPeople, Person, TypeMeeting, CampaignCharge, Campaign, Surveyed
from django_mptt_admin.admin import DjangoMpttAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from .forms import MeetingForm
from .resources import PersonResource, ListPeopleResource


# Register your models here.


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin, ExportActionMixin):
    resource_class = PersonResource
    # form = PersonForm
    list_display = ('id', 'first_name', 'last_name', 'sex', 'identification_card', 'cellphone', 'email', 'is_voter',
                    'campaign_charge', 'parent')
    list_filter = ('sex', 'is_voter', )
    # raw_id_fields = ('assistant', )
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
    exclude = ('campaign', )
    autocomplete_fields = ['person', 'meeting']


@admin.register(Meeting)
class MeetingAdmin(ImportExportModelAdmin, ExportActionMixin, ):
    form = MeetingForm
    list_display = ('id', 'date', 'start_time', 'end_time')
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

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'candidature', None) is None:
            print('CAMPAÑA DEL USER LOGUEADO: ', request.user.campaign)
            obj.candidature = request.user.campaign
        obj.save()

    def get_form(self, request, *args, **kwargs):
        form = super(MeetingAdmin, self).get_form(request, *args, **kwargs)
        form.current_user = request.user
        return form

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(candidature=request.user.campaign)


@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('id', 'name', 'number', 'political_party')
    search_fields = ('name', 'number', 'political_party__name')
    autocomplete_fields = ['political_party']

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(id=request.user.campaign.id)


@admin.register(CampaignCharge)
class CampaignChargeAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('id', 'name', 'parent')
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
class TypeMeetignAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('id', 'name',)
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
class ListPeopleAdmin(ImportExportModelAdmin, ExportActionMixin):
    resource_class = ListPeopleResource
    list_display = ('id', 'date', 'country', 'state', 'city', 'zone', 'ubication')
    search_fields = ('date', 'country__name', 'state__name', 'city__name', 'zone__name', 'ubication')
    exclude = ('campaign', )
    autocomplete_fields = ['country', 'state', 'city', 'zone']
    inlines = [SurveyedInline]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                'date', 'country', 'state', 'city', 'zone', 'ubication')
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


@admin.register(Surveyed)
class SurveyedAdmin(ImportExportModelAdmin, ExportActionMixin):
    # resource_class = SurveyedResource
    list_display = ('id', 'list_people', 'person', 'meeting', 'campaign',)
    search_fields = ('campaign__name',)
    exclude = ('campaign', )
    autocomplete_fields = ['campaign', 'person', 'list_people', 'meeting']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('list_people', 'person', 'meeting')
        }),
    )

    suit_form_tabs = (
        ('general', 'Encuestado'),
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
