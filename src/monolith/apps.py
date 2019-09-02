from django.contrib import admin
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('Mi Campaña', icon='fa fa-users', children=[
            ChildItem(model='campaigns.campaign'),
            ChildItem(model='campaigns.meeting'),
            ChildItem(model='campaigns.listpeople'),
            ChildItem(model='campaigns.surveyed'),
            ChildItem(model='campaigns.person'),
            ChildItem(model='campaigns.typemeeting'),
            ChildItem(model='campaigns.campaigncharge'),
        ]),
        ParentItem('Ubicaciones', icon='fa fa-map-marker', children=[
            ChildItem(model='locations.country'),
            ChildItem(model='locations.region'),
            ChildItem(model='locations.city'),
            ChildItem(model='locations.zone'),
            ChildItem(model='locations.neighborhood'),
            ChildItem(model='locations.votingpost'),
        ]),
        ParentItem('Clientes', icon='fa fa-user', children=[
            ChildItem(model='users.user'),
            ChildItem(model='auth.group'),
        ]),
        ParentItem('Configuración', icon='fa fa-cog', children=[
            ChildItem(model='configurations.politicalparty'),
        ]),
        ParentItem('Clientes', icon='fa fa-bug', children=[
            # ChildItem(model='campaigns.campaign'),
        ]),
    )
