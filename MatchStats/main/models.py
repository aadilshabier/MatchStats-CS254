from django.db import models
from django.core.exceptions import ValidationError




# Create your models here.

class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=50, null = False)
    team_code = models.CharField(max_length=3)
    home_stadium = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()
    points = models.IntegerField()


class Player(models.Model):
    POSITION = [
        ('G',"Goalkeeper"),
        ('D',"Defender"),
        ('M',"Midfielder"),
        ('F',"Forward"),
    ]

    p_id = models.IntegerField(primary_key = True)
    p_name = models.CharField(max_length=50)
    # team = models.CharField(max_length=50)
    jersey_no = models.PositiveSmallIntegerField()
    dob = models.DateField( null = False, blank = False)
    position = models.CharField(choices=POSITION, max_length=1)
    team_id = models.ForeignKey(Teams, to_field = 'team_id' ,on_delete = models.SET_NULL, null = True)
    goals = models.IntegerField(default=0, null = True)
    assists = models.IntegerField(default=0, null = True)
    yellow_cards = models.IntegerField(default=0, null = True)
    red_cards = models.IntegerField(default=0, null = True)

class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length= 200)
    city = models.CharField(max_length=50)
    capacity = models.IntegerField(default = 0)

class Matches(models.Model):
    match_id = models.IntegerField(primary_key=True)
    team_1 = models.ForeignKey(Teams,related_name='team_1', to_field='team_id', on_delete= models.CASCADE)
    team_2 = models.ForeignKey(Teams,related_name='team_2', to_field='team_id', on_delete= models.CASCADE)
    score_1 = models.PositiveSmallIntegerField(default= 0 )
    score_2 = models.PositiveSmallIntegerField(default = 0)
    match_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    stadium_id = models.ForeignKey(Stadium, to_field='stadium_id', on_delete=models.CASCADE)
    viewer_count = models.PositiveIntegerField(default=0)

class Transfers(models.Model):
    transfer_id = models.IntegerField(primary_key=True)
    team_from_id = models.ForeignKey(Teams, related_name = 'team_from', to_field= 'team_id', on_delete=models.CASCADE)
    team_to_id = models.ForeignKey(Teams, related_name = 'team_to',to_field='team_id', on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, to_field='p_id', on_delete=models.CASCADE)
    price = models.FloatField()
    transfer_date = models.DateField( null = False, blank = False)


class SupportStaff(models.Model):
    STAFF_JOB_LIST = [
        ('mgr', 'Manager'),
        ('ch', 'Coach')
    ]
    staff_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(choices=STAFF_JOB_LIST, max_length=20)
    team_id = models.ForeignKey(Teams, to_field='team_id', on_delete=models.CASCADE)

class Goals(models.Model):
    goal_id = models.IntegerField()
    match_id = models.ForeignKey(Matches, to_field='match_id', on_delete=models.CASCADE)
    team_id = models.ForeignKey(Teams, to_field = 'team_id' ,on_delete = models.SET_NULL, null = True)
    player_id = models.ForeignKey(Player,related_name='player', to_field='p_id', on_delete=models.CASCADE)
    assist_id = models.ForeignKey(Player, related_name='assist',to_field='p_id', on_delete=models.CASCADE)
    match_time = models.DateTimeField()
    