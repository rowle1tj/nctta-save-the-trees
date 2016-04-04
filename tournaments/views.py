from django.shortcuts import render
from tournaments.models import Roster
from django.db.models import Q

# Create your views here.
def index(request):
    # get a list of rosters if the logged in user is the captain
    if request.user.is_authenticated():
        if request.user.profile.is_captain:
            profile = request.user.profile
            incomplete_rosters = Roster.objects.filter(
                Q(left_team__college=profile.college, active_team='left') |
                Q(right_team__college=profile.college, active_team='right')
            )

            for roster in incomplete_rosters:
                if roster.active_team == 'left':
                    print roster.left_team
                else:
                    print roster.right_team


    context = {}
    return render(request, 'tournaments/home_page.html', context)

def index_old(request):
    context = {}
    return render(request, 'tournaments/backup_home_page.html', context)
