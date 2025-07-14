from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("stream" , views.StreamPlatform , basename="streamplatform")
urlpatterns = [
    path("list/" , views.WatchList.as_view(), name="movie_list" ),
    path("<int:pk>/" , views.WatchDetailAV.as_view() , name="movie_detail"),
    # path("stream/",views.StreamPlatformAV.as_view() , name ="stream"),
    # path("stream/<int:pk>/" , views.StreamDetailAV.as_view(), name="stream_detail"),
    path("" , include(router.urls)),
    
    # path("stream/<int:pk>/review"),
    # path("watch/<int:pk>/review"),


    # path("reviews/" ,views.ReviewList.as_view(), name="review_list" ),
    path('<int:pk>/review' , views.ReviewList.as_view() , name="review_list"),
    path('<int:pk>/review/create' , views.ReviewCreate.as_view() , name="review-create"),
    path("review/<int:pk>" ,views.ReviewDetail.as_view(), name="review_list" ),


     path("review/" ,views.UserReview.as_view(), name="user-review" )
]

#/watch