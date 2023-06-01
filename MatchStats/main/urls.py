from django.urls import path

from . import views
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("teams/", views.TeamsList.as_view(), name = "team_list"),
    path("team/<int:pk>/", views.TeamDetail.as_view(), name="team_detail"),
    path("match/<int:pk>/", views.MatchDetail.as_view(), name="match_detail"),
    path('player/<int:pk>/', views.PlayerDetail.as_view(), name='player_detail'),
    path("transfer/<int:pk>/", views.TransferDetail.as_view(), name="transfer_detail"),
    path("matches/", views.MatchList.as_view(), name="match_list"),
    path("stadiums/", views.StadiumList.as_view(), name="stadium_list"),
    path('players/',views.PlayersList.as_view(),name="player_list"),
    path('transfers/', views.TransferList.as_view(), name="transfer_list"),
    path('player/<int:pk>/update/',views.PlayerUpdateView.as_view(), name="player_update"),
    path('team/<int:pk>/update/',views.TeamUpdateView.as_view(), name="team_update"),
    path('match/<int:pk>/update',views.MatchUpdateView.as_view(), name="match_update"),
    path('table/',views.PointsTable.as_view(), name="points_table"),
]