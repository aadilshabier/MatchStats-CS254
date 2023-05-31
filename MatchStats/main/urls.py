from django.urls import path

from . import views
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("teams/", views.TeamsList.as_view(), name = "team_list"),
    path("team/<int:pk>/", views.TeamDetail.as_view(), name="team_detail"),
    path("match/<int:pk>/", views.MatchDetail.as_view(), name="match_detail"),
    path("matches/", views.MatchList.as_view(), name="match_list"),
    path("stadiums/", views.StadiumList.as_view(), name="stadium_list"),
    path('player/<int:pk>/', views.PlayerDetail.as_view(), name='player_detail'),
    path('players/',views.PlayersList.as_view(),name="player_list"),
]