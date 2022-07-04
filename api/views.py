from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.

from .serializers import MatchSerialiser, TeamSerialiser, PlayerSerialiser, TeamPlayerSerialiser, GoalSerialiser, UserSerialiser
from .models import Match, Team, Player, TeamPlayer, Goal
from django.contrib.auth.models import User


# MATCHES

@api_view(['GET', 'POST'])
def handle_matches(request):
    if request.method == 'GET':
        matches = Match.objects.all()
        serializer = MatchSerialiser(matches, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        teamA = Team.objects.create(team_name="Team A", is_default=True)
        teamB = Team.objects.create(team_name="Team B", is_default=True)
        match = Match.objects.create(
            team_a=teamA, team_b=teamB, start_time=request.data['start_time'], end_time=request.data['end_time'], location=request.data['location'])
        serializer = MatchSerialiser(match)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_match(request, match_id):
    if request.method == 'GET':
        match = Match.objects.get(unique_id=match_id)
        serializer = MatchSerialiser(match)
        return Response(serializer.data)
    elif request.method == 'PUT':
        match = Match.objects.get(unique_id=match_id)
        # Here we can update the match no matter what the request is
        for key, value in request.data.items():
            setattr(match, key, value)
        match.save()
        serializer = MatchSerialiser(match)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        match = Match.objects.get(unique_id=match_id)
        match.delete()
        return Response("Match deleted")


@api_view(['GET'])
def get_match_goals(request, match_id):
    if request.method == 'GET':
        goals = Goal.objects.filter(match_id=match_id)
        serializer = GoalSerialiser(goals, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def handle_match_per_team_goals(request, match_id, team):
    if request.method == 'GET':
        match = Match.objects.get(unique_id=match_id)
        team_id = ""
        if team == "team_a":
            team_id = match.team_a
        elif team == "team_b":
            team_id = match.team_b
        goals = Goal.objects.filter(match=match, team=team_id)
        serializer = GoalSerialiser(goals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        match = Match.objects.get(unique_id=match_id)
        team_id = ""
        if team == "team_a":
            team_id = match.team_a
        elif team == "team_b":
            team_id = match.team_b
        goal = Goal.objects.create(
            match=match, team=team_id)
        serializer = GoalSerialiser(goal)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_match_per_team_goal(request, match_id, team, goal_id):
    if request.method == 'GET':
        goal = Goal.objects.get(unique_id=goal_id)
        serializer = GoalSerialiser(goal)
        return Response(serializer.data)
    elif request.method == 'PUT':
        goal = Goal.objects.get(unique_id=goal_id)
        if 'player' in request.data:
            player = Player.objects.get(unique_id=request.data['player'])
            goal.player = player
        if 'goal_time' in request.data:
            goal.goal_time = request.data['goal_time']
        goal.save()
        serializer = GoalSerialiser(goal)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        goal = Goal.objects.get(unique_id=goal_id)
        goal.delete()
        return Response("Goal deleted")

# TEAMS


@api_view(['GET', 'POST'])
def handle_teams(request):
    if request.method == 'GET':
        teams = Team.objects.filter(is_default=request.data['is_default'])
        serializer = TeamSerialiser(teams, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        team = Team.objects.create(team_name=request.data['team_name'])
        serializer = TeamSerialiser(team)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_team(request, team_id):
    if request.method == 'GET':
        team = Team.objects.get(
            unique_id=team_id)
        serializer = TeamSerialiser(team)
        return Response(serializer.data)
    elif request.method == 'PUT':
        team = Team.objects.get(unique_id=team_id)
        # Here we can update the match no matter what the request is
        for key, value in request.data.items():
            setattr(team, key, value)
        team.save()
        serializer = TeamSerialiser(team)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        team = Team.objects.get(unique_id=team_id)
        team.delete()
        return Response("Team deleted")

# PLAYERS


@api_view(['GET', 'POST'])
def handle_players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerialiser(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        player = Player.objects.create(player_name=request.data['player_name'], phone_number=request.data['phone_number'],
                                       email=request.data['email'], nationality=request.data['nationality'], user_pic=request.data['user_pic'])
        serializer = PlayerSerialiser(player)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_player(request, player_id):
    if request.method == 'GET':
        player = Player.objects.get(unique_id=player_id)
        serializer = PlayerSerialiser(player)
        return Response(serializer.data)
    elif request.method == 'PUT':
        player = Player.objects.get(unique_id=player_id)
        # Here we can update the match no matter what the request is
        for key, value in request.data.items():
            setattr(player, key, value)
        player.save()
        serializer = PlayerSerialiser(player)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        player = Player.objects.get(unique_id=player_id)
        player.delete()
        return Response("Player deleted")

# TEAM PLAYERS


@api_view(['GET'])
def handle_team_players(request, team_id):
    if request.method == 'GET':
        team_players = TeamPlayer.objects.filter(team=team_id)
        serializer = TeamPlayerSerialiser(team_players, many=True)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def handle_team_player(request, team_id, player_id):
    if request.method == 'POST':
        team = Team.objects.get(unique_id=team_id)
        player = Player.objects.get(unique_id=player_id)
        team_player = TeamPlayer.objects.create(team=team, player=player)
        serializer = TeamPlayerSerialiser(team_player)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        team = Team.objects.get(unique_id=team_id)
        player = Player.objects.get(unique_id=player_id)
        team_player = TeamPlayer.objects.get(team=team, player=player)
        team_player.delete()
        return Response("Team player deleted")

# GOALS


@api_view(['GET', 'POST'])
def get_all_goals(request):
    if request.method == 'GET':
        goals = Goal.objects.all()
        serializer = GoalSerialiser(goals, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_all_goal(request, goal_id):
    if request.method == 'GET':
        goal = Goal.objects.get(unique_id=goal_id)
        serializer = GoalSerialiser(goal)
        return Response(serializer.data)


# USERS

@api_view(['GET', 'POST'])
def handle_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerialiser(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user = User.objects.create(username=request.data['username'], password=request.data['password'], email=request.data['email'])
        if 'invitation_code' in request.data:
            player = Player.objects.get(
                unique_id=request.data['invitation_code'])
            player.user = user
            player.save()
        serializer = UserSerialiser(user)
        return Response(serializer.data)
