from typing import override

from watchlist_app.models import WatchList , StreamPlatform , Review
from .serializers import WatchListSerializer , StreamPlatformSerializer , ReviewSerializer

from rest_framework.response import Response, Serializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from watchlist_app.api.permissions import IsAdminOrReadOnly , IsReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle , AnonRateThrottle
from watchlist_app.api.throttling import ReviewCreateThrottle,ReviewListThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from watchlist_app.api.pagination import WatchListPaginaion


class UserReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]
 
    # def get_queryset(self):
    #     username = self.kwargs["username"]
    #     return Review.objects.filter(review_user__username = username)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username = username)


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    throttle_classes = [ReviewCreateThrottle]
    

    def perform_create(self,serializer):
        pk = self.kwargs["pk"]
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_query = Review.objects.filter(watchlist = watchlist , review_user = review_user)
        if review_query.exists():
            raise ValidationError("You already submitted a review")

        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data["rating"])/2
        
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        serializer.save(watchlist=watchlist , review_user= review_user)
       
    

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']

    @override
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist = pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = [UserRateThrottle]


# class ReviewList(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request , *args, **kwargs)

#     def post(self,request,*args, **kwargs):
#         return self.create(request , *args, **kwargs)


# class StreamPlatform(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

class StreamPlatform(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer



class StreamPlatformAV(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self , request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform , many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

class StreamDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)

    def put(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(instance=stream , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        stream = get_object_or_404(StreamPlatform, pk=pk )
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

        

class WatchList(generics.ListAPIView):
    queryset= WatchList.objects.all()
    serializer_class = WatchListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
    pagination_class = WatchListPaginaion





class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    


    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies , many=True)
        return Response(serializer.data)

    def post(self , request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)

 
class WatchDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self , request , pk):
        movie = get_object_or_404(WatchList, pk=pk )
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self , request ,pk):
        movie = get_object_or_404(WatchList, pk=pk )
        serializer = WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movie = get_object_or_404(WatchList, pk=pk )
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# FUNCTION BASED VIEWS

# @api_view(['GET' , 'POST'])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies , many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         print(request.data)
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET' ,'DELETE' , "PUT"])
# def movie_detail(req , pk):
    # movie = get_object_or_404(Movie, pk=pk )
#     if (req.method == 'GET'):
        # serializer = MovieSerializer(movie)
        # return Response(serializer.data)

#     if (req.method == "PUT"):
        # serializer = MovieSerializer(instance=movie, data=req.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if req.method == "DELETE":
        # movie.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)