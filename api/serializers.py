from rest_framework.serializers import ModelSerializer
from .models import Match, Team, Player, TeamPlayer, Goal, PlayerPerMatch
from django.contrib.auth.models import User


class MatchSerialiser(ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PlayerPerMatchSerialiser(ModelSerializer):
    class Meta:
        model = PlayerPerMatch
        fields = '__all__'

class TeamSerialiser(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerialiser(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamPlayerSerialiser(ModelSerializer):
    class Meta:
        model = TeamPlayer
        fields = '__all__'

class GoalSerialiser(ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class UserSerialiser(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'