from django.shortcuts import render
from django.views import generic

from .models import Stadium, Player, Team, Match

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

class TeamsList(generic.ListView):
    model = Team
    template_name = 'main/team_list.html'
    context_object_name = "teams"
    ordering = ["-points"]

class TeamDetail(generic.DetailView):
    model = Team
    template_name = 'main/team_detail.html'

class StadiumList(generic.ListView):
    model = Stadium
    template_name = 'main/stadium_list.html'
    context_object_name = "stadiums"

class MatchList(generic.ListView):
    model = Match
    template_name = 'main/match_list.html'
    context_object_name = "matches"
    ordering = ["match_time"]

class MatchDetail(generic.DetailView):
    model = Match
    template_name = 'main/match_detail.html'

class PlayerDetail(generic.DetailView):
    model = Player
    template_name = 'main/player_detail.html'

class PlayersList(generic.ListView):
    model = Player
    template_name = 'main/player_list.html'
    context_object_name = "players"
       