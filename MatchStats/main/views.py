from django.shortcuts import render
from django.http import HttpResponse

from .models import Stadium, Player, Team, Match, Goal

from django.views.generic import ListView, DetailView

def index(request):
    return HttpResponse(b"MatchStats app")

class TeamsList(ListView):
    model = Team
    template_name = 'main/team_list.html'

class TeamDetail(DetailView):
    model = Team
    template_name = 'main/team_detail.html'

class StadiumList(ListView):
    model = Stadium
    template_name = 'main/stadium_list.html'

class MatchList(ListView):
    model = Match
    template_name = 'main/match_list.html'


class MatchDetail(DetailView):
    model = Match
    template_name = 'main/match_detail.html'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'main/player_detail.html'

class PlayersList(ListView):
    model = Player
    template_name = 'main/player_list.html'
