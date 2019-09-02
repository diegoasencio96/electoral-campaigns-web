from import_export import resources
from .models import Person, Meeting, ListPeople


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        import_id_fields = ('id',)
        fields = ('id', 'campaign__id', 'list_people', 'first_name', 'last_name', 'sex', 'year_old', 'identification_card', \
                  'cellphone', 'email', 'country__id', 'state__id', 'city__id', 'zone__id', 'sector__id', 'address', 'voting_post__id', 'is_voter', \
                  'campaign_charge__id', 'parent__id')


class ListPeopleResource(resources.ModelResource):
    class Meta:
        model = ListPeople
        import_id_fields = ('id',)
        fields = ('id', 'campaign__id', 'campaign__id', 'id_list', 'date', 'country__id', 'state__id', 'city__id', 'zone__id', 'ubication', )

