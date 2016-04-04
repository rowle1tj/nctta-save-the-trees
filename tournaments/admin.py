from django.contrib import admin
from tournaments.models import Tournament, Team, TeamPlayer, Roster

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(TeamPlayer)
admin.site.register(Roster)
