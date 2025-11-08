from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CountryListAPIView, CountryDetailAPIView,
                    DirectorListAPIView, DirectorDetailAPIView,
                    ActorListAPIView,
                    GenreListAPIView, MovieListAPIView, MovieDetailAPIView,
                    MovieLanguagesListAPIView, MomentsListAPIView,
                    FavoriteViewSet, FavoriteMovieViewSet, HistoryListAPIView, RatingViewSet,
                    RegisterView, CustomLoginView, LogoutView, ActorDetailAPIView, GenreDetailAPIView)


router = routers.SimpleRouter()
router.register('users', UserProfileViewSet)
router.register('favorite', FavoriteViewSet)
router.register('favorite_movie', FavoriteMovieViewSet)
router.register('rating', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('movies/', MovieLanguagesListAPIView.as_view(), name='movies'),
    path('country/', CountryListAPIView.as_view(), name='country'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('director/', DirectorListAPIView.as_view(), name='director'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor-list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre-list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('moments/', MomentsListAPIView.as_view(), name='moments'),
    path('history/', HistoryListAPIView.as_view(), name='history'),
]
