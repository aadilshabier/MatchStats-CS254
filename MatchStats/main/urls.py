from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("teams", views.TeamsList.as_view(), name = "team_list"),
    path("team/<int:team_id>", views.TeamDetail.as_view(), name="teamDetail"),
    path("match/<int:match_id>", views.MatchDetail.as_view(), name="matchDetail"),
    path("matches", views.MatchList.as_view(), name="match_list"),
    path("stadiums", views.StadiumList.as_view(), name="stadium_list"),
]