
from django.urls import path
from django.http import HttpResponse
from . import views


def hello_world(request):
    return HttpResponse('Hello, World!')


urlpatterns = [
    path('', hello_world),
    path('matches/', views.handle_matches),
    path('matches/<str:match_id>/', views.handle_match),
    path('matches/<str:match_id>/goals/', views.get_match_goals),  
    path('matches/<str:match_id>/goals/<str:team>/', views.handle_match_per_team_goals),
    path('matches/<str:match_id>/goals/<str:team>/<str:goal_id>/', views.handle_match_per_team_goal),
    path('teams/', views.handle_teams),
    path('teams/<str:team_id>/', views.handle_team),
    path('teams/<str:team_id>/players/', views.handle_team_players),
    path('teams/<str:team_id>/players/<str:player_id>/', views.handle_team_player),
    path('players/', views.handle_players),
    path('players/<str:player_id>/', views.handle_player),
    path('goals/', views.get_all_goals),
    path('goals/<str:goal_id>/', views.get_all_goal),
    path('users/', views.handle_users),
]
