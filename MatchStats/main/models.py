from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Stadium(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=64)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=3, unique=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True, blank=True)
    played = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    losses = models.PositiveSmallIntegerField(default=0)
    goals_for = models.PositiveSmallIntegerField(default=0)
    goals_against = models.PositiveSmallIntegerField(default=0)
    points = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION = [
        ('G',"Goalkeeper"),
        ('D',"Defender"),
        ('M',"Midfielder"),
        ('F',"Forward"),
    ]

    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete = models.SET_NULL)
    jersey_no = models.PositiveSmallIntegerField(null=True)
    dob = models.DateField()
    position = models.CharField(max_length=1, choices=POSITION)
    goals = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    yellow_cards = models.PositiveSmallIntegerField(default=0)
    red_cards = models.PositiveSmallIntegerField(default=0)
    nationality = models.CharField(max_length=64)
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Match(models.Model):
    team_1 = models.ForeignKey(Team, null=True, related_name="team_1", on_delete=models.SET_NULL)
    team_2 = models.ForeignKey(Team, null=True, related_name="team_2", on_delete=models.SET_NULL)
    score_1 = models.PositiveSmallIntegerField(default=0)
    score_2 = models.PositiveSmallIntegerField(default=0)
    shots_1 = models.PositiveSmallIntegerField(default=0)
    shots_2 = models.PositiveSmallIntegerField(default=0)
    offsides_1 = models.PositiveSmallIntegerField(default=0)
    offsides_2 = models.PositiveSmallIntegerField(default=0)
    corners_1 = models.PositiveSmallIntegerField(default=0)
    corners_2 = models.PositiveSmallIntegerField(default=0)
    match_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    stadium = models.ForeignKey(Stadium, null=True, on_delete=models.SET_NULL)
    viewer_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.team_1.code + " vs " + self.team_2.code

class Transfer(models.Model):
    team_from = models.ForeignKey(Team, null=True, related_name="team_from", blank=True, on_delete=models.SET_NULL)
    team_to = models.ForeignKey(Team, null=True, related_name="team_to", blank=True, on_delete=models.SET_NULL)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    transfer_date = models.DateField()

class Staff(models.Model):
    STAFF_JOB_LIST = [
        ('tstaff', 'Tournament Staff'),
        ('mgr', 'Manager'),
        ('staff', 'Staff')
    ]
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(choices=STAFF_JOB_LIST, max_length=20)
    team_id = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete = models.SET_NULL)
    scorer = models.ForeignKey(Player, null=True, related_name="goal_set", on_delete=models.SET_NULL)
    assister = models.ForeignKey(Player, null=True, related_name="assist_set",blank=True, on_delete=models.SET_NULL)
    match_time = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120)])