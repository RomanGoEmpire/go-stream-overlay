from django.urls import path

from . import views


app_name = "database"
urlpatterns = [
    path("", views.index, name="index"),
    path("tournament/<int:tournament_id>/", views.tournament, name="tournament"),
    path("round/<int:round_id>/", views.round, name="round"),
    path("game/<int:game_id>/", views.game, name="game"),
    path("person/<int:person_id>/", views.person, name="person"),
    path("person_list/", views.person_list, name="person_list"),
    path("new_person/", views.new_person, name="new_person"),
]
