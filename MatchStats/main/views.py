from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from .models import Stadium, Player, Team, Match, Transfer, Staff
from django.contrib.auth.models import User

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

class TeamsList(generic.ListView):
    model = Team
    template_name = 'main/team_list.html'
    context_object_name = "teams"
    ordering = ["name"]

class PointsTable(generic.ListView):
    model = Team
    template_name = 'main/points_table.html'
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
    ordering = ['name']

class TransferList(generic.ListView):
    model = Transfer
    template_name = "main/transfer_list.html"
    context_object_name = "transfers"
    ordering = ['-transfer_date']

class TransferFilteredList(generic.ListView):
    model = Transfer
    template_name = "main/transfer_list.html"
    context_object_name = "transfers"
    ordering = ['-transfer_date']

    def get_queryset(self):
        qs = super().get_queryset()
        user  = User.objects.get(pk=self.kwargs['user_id'])
        if user.username == 'admin':
            return qs
        elif not Staff.objects.filter(user_id=user):
            return None
        team = user.staff.team_id
        return qs.filter(team_from=team) | qs.filter(team_to=team)

class TransferDetail(generic.DetailView):
    model = Transfer
    template_name = "main/transfer_detail.html"

class TeamUpdateView(generic.UpdateView):
    model=Team
    fields = '__all__'
    template_name = 'main/team_update.html'
    def get_success_url(self):
        return reverse('main:team_detail', kwargs={'pk' : self.object.pk})
      

class PlayerUpdateView(generic.UpdateView):
    model = Player
    fields = ['name','team','jersey_no','dob','position','goals','assists','yellow_cards','red_cards','nationality','height']
    template_name = 'main/player_update.html'
    def get_success_url(self):
        return reverse('main:player_detail', kwargs={'pk' : self.object.pk})
      

class MatchUpdateView(generic.UpdateView):
    model = Match
    fields = '__all__'
    template_name = 'main/match_update.html'
    def get_success_url(self):
        return reverse('main:match_detail', kwargs={'pk' : self.object.pk})
      
   