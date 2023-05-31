from django.urls import reverse_lazy
from django.views import generic
from .models import Stadium, Player, Team, Match, Transfer

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

class TransferList(generic.ListView):
    model = Transfer
    template_name = "main/transfer_list.html"
    context_object_name = "transfers"

class TransferDetail(generic.DetailView):
    model = Transfer
    template_name = "main/transfer_detail.html"

class TeamUpdateView(generic.UpdateView):
    model=Team
    fields = '__all__'
    template_name = 'main/team_update.html'
    success_url = reverse_lazy('team/<int:pk>/')


class PlayerUpdateView(generic.UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'main/player_update.html'
    success_url = reverse_lazy('player/<int:pk>/')

class MatchUpdateView(generic.UpdateView):
    model = Match
    fields = '__all__'
    template_name = 'main/match_update.html'
    success_url = reverse_lazy('match/<int:pk>/')
   