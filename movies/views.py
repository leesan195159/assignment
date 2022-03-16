import json
from .models import Actor, Movie
from django.http import JsonResponse
from django.views import View

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = [{
            'first_name'  : actor.first_name,
            'last_name'   : actor.last_name,
            'movies_list' : [{
                'title' : movie.title
            }for movie in actor.movies.all()]
        }for actor in actors]

        return JsonResponse({'Result' : results}, status = 201)


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = [{
            'title' : movie.title,
            'running_time' : movie.running_time,
            'actors_list' : [{
                'name' : actor.first_name
            }for actor in movie.actor_set.all()]
        }for movie in movies]

        return JsonResponse({'Result' : results}, status = 201)