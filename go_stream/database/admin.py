from django.contrib import admin

from .models import Person, Sponsor, Organizer, Tournament, Round, Game, Selected

admin.site.register([Person, Sponsor, Organizer, Tournament, Round, Game, Selected])
