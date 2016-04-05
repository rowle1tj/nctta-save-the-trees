from django.db import models
from django.contrib.auth.models import User
from tournaments.utility_functions import get_rosters_from_excel
from nctta_org.models import College

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=255)
    excel_document = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Tournament, self).save(*args, **kwargs)
        # for now every time we save the tournament will we generate the other objects.  later i will change it so that it only does it if it is new
        rosters = get_rosters_from_excel(self.excel_document)
        for r in rosters:
            roster = Roster.objects.filter(active_team=r["active_team"], left_team__name=r["left_team_title"], right_team__name=r["right_team_title"], tournament=self)
            if len(roster) == 0:
                roster = Roster()
            else:
                roster = roster[0]

            roster.round_match = r["round_match"]
            left_team = Team.objects.filter(tournament=self, name=r["left_team_title"])
            if len(left_team) == 0:
                left_team = Team()
            else:
                left_team = left_team[0]
            left_team.name = r["left_team_title"]
            left_team.label = r["left_team_label"]
            left_team.tournament = self
            left_team.save()
            roster.left_team = left_team

            right_team = Team.objects.filter(tournament=self, name=r["right_team_title"])
            if len(right_team) == 0:
                right_team = Team()
            else:
                right_team = right_team[0]
            right_team.name = r["right_team_title"]
            right_team.label = r["right_team_label"]
            right_team.tournament = self
            right_team.save()
            roster.right_team = right_team

            roster.active_team = r["active_team"]

            if roster.active_team == "left":
                active_team = left_team
                opposing_team = right_team
            else:
                active_team = right_team
                opposing_team = left_team


            order_id = 0
            for player in r["players"]:
                if player["player_name"].strip() != "":
                    pname = player["player_name"]
                    plabel = player["player_label"]
                    player = TeamPlayer.objects.filter(name=pname, team=active_team, tournament=self)
                    if len(player) == 0:
                        player = TeamPlayer()
                    else:
                        player = player[0]
                    player.name = pname
                    player.label = plabel
                    player.order_id = order_id
                    player.team = active_team
                    player.tournament = self
                    player.save()
                    order_id += 1

            for player in r["opponents"]:
                if player["player_name"].strip() != "":
                    pname = player["player_name"]
                    prating = player["player_rating"]
                    player = TeamPlayer.objects.filter(name=pname, team=opposing_team, tournament=self)
                    if len(player) == 0:
                        player = TeamPlayer()
                    else:
                        player = player[0]
                    player.name = pname
                    player.rating = prating
                    player.team = opposing_team
                    player.tournament = self
                    player.save()

            roster.tournament = self
            roster.save()


        super(Tournament, self).save(*args, **kwargs)

class Team(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    owning_user = models.ForeignKey(User, blank=True, null=True)
    college = models.ForeignKey(College, blank=True, null=True)
    tournament = models.ForeignKey("Tournament")

    def __unicode__(self):
        return self.name

class TeamPlayer(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    rating = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey("Team")
    tournament = models.ForeignKey("Tournament")

    def __unicode__(self):
        return self.name

class Roster(models.Model):
    left_team = models.ForeignKey("Team", related_name="left_team", null=True, blank=True)
    right_team = models.ForeignKey("Team", related_name="right_team", null=True, blank=True)
    round_match = models.CharField(max_length=255)
    active_team = models.CharField(max_length=255, choices=(("left", "left"), ("right", "right")))
    tournament = models.ForeignKey("Tournament", blank=True, null=True)

    player1 = models.ForeignKey("TeamPlayer", related_name="player1", blank=True, null=True)
    player2 = models.ForeignKey("TeamPlayer", related_name="player2", blank=True, null=True)
    player3 = models.ForeignKey("TeamPlayer", related_name="player3", blank=True, null=True)
    player4 = models.ForeignKey("TeamPlayer", related_name="player4", blank=True, null=True)
    doubles_partner = models.ForeignKey("TeamPlayer", blank=True, null=True)
    completed_datetime = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.round_match + " - " + self.active_team

    def get_active_players(self):
        if self.active_team == 'left':
            return TeamPlayer.objects.filter(team=self.left_team).order_by('order_id')
        else:
            return TeamPlayer.objects.filter(team=self.right_team).order_by('order_id')


    def get_opponent_players(self):
        if self.active_team == 'left':
            return TeamPlayer.objects.filter(team=self.right_team).order_by('order_id')
        else:
            return TeamPlayer.objects.filter(team=self.left_team).order_by('order_id')
                
            
