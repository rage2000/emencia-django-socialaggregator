"""Admin for parrot.gallery"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from socialaggregator.models import Feed
from socialaggregator.models import Aggregator
from socialaggregator.models import Ressource


class FeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feed, FeedAdmin)


class AggregatorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aggregator, AggregatorAdmin)


class RessourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ressource, RessourceAdmin)