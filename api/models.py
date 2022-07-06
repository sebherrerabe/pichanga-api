from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Player(models.Model):
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    player_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    user_pic = models.TextField(max_length=255, blank=True, null=True)
    main_team = models.ForeignKey(
        'Team', on_delete=models.SET_DEFAULT, default=None, null=True)


class Team(models.Model):
    unique_id = models.UUIDField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    team_name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=None, null=True)


class Match(models.Model):
    unique_id = models.UUIDField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    team_a = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team_a')
    team_b = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team_b')
    team_a_score = models.IntegerField(default=0)
    team_b_score = models.IntegerField(default=0)
    players_number = models.IntegerField(default=0)
    match_date = models.DateTimeField(auto_now_add=True)
    match_result = models.CharField(max_length=100, default="draw")
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organised_by = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)


class TeamPlayer(models.Model):
    unique_id = models.UUIDField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class PlayerPerMatch(models.Model):
    unique_id = models.UUIDField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Goal(models.Model):
    unique_id = models.UUIDField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=None, null=True, blank=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goal_time = models.TimeField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.SET_DEFAULT, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



User._meta.get_field('email').blank = False