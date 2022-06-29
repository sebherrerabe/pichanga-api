from django.contrib import admin

# Register your models here.

from .models import Player, Team, Match, TeamPlayer, Goal

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(TeamPlayer)
admin.site.register(Goal)
