# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(req):
#     movies = Movie.objects.all()
#     data = {"movies" : list(movies.values())}
    
#     return JsonResponse(data)


# def movie_detail(req , pk):
#     movie = Movie.objects.get(pk=pk)
   
#     data = {
#         "name" : movie.name,
#         "des"  : movie.description,
#         "active" : movie.active
#     }

#     return JsonResponse(data)