from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tournament, Round, Game, Person
from .forms import PersonForm


def index(request):
    return HttpResponse("Hello, world. You're at the database index.")


def tournament(request, tournament_id):
    return HttpResponse(f"You're looking at tournament {tournament_id}.")


def round(request, round_id):
    return HttpResponse(f"You're looking at round {round_id}.")


def game(request, game_id):
    return HttpResponse(f"You're looking at game {game_id}.")


def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "person.html", {"person": person})


def person_list(request):
    person_list = Person.objects.all()
    context = {"person_list": person_list}
    return render(request, "person_list.html", context)


def new_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("database:person_list")
    else:
        form = PersonForm()

    return render(request, "new_person.html", {"form": form})
