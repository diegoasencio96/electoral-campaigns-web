from django.contrib import admin
from .models import Meeting, ListPeople, Person, TypeMeeting, CampaignCharge, Campaign
from django_mptt_admin.admin import DjangoMpttAdmin
# Register your models here.


@admin.register(Person)
class PersonAdmin(DjangoMpttAdmin):
    # resource_class = PersonResource
    # form = PersonForm
    list_display = ('first_name', 'last_name', 'sex', 'identification_card', 'cellphone', 'email', 'is_voter',
                    'campaign_charge', 'parent')
    list_filter = ('sex', 'is_voter', 'country', 'state', 'city', 'zone', 'sector', 'voting_post', )
    # raw_id_fields = ('assistant', )
    suit_list_filter_horizontal = ('campaign_charge', 'parent')
    search_fields = ('first_name', 'last_name', 'identification_card', 'cellphone', 'email', 'address')
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

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        return queryset.all()


class SurveyedInline(admin.TabularInline):
    model = Person.list_people.through
    extra = 1
    suit_classes = 'suit-tab suit-tab-list'


class ListPeopleAdmin(admin.ModelAdmin):
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


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidature', 'date', 'start_time', 'end_time')
    list_filter = ('type_activity',)
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
        return queryset # .filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'candidature', None) is None:
            obj.candidature = request.user.campaign
        obj.save()


admin.site.register(ListPeople, ListPeopleAdmin)
admin.site.register(TypeMeeting)
admin.site.register(CampaignCharge)
admin.site.register(Campaign)