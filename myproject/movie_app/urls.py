from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CountryListAPIView, DirectorListAPIView, ActorListAPIView,
                    GenreListAPIView, MovieViewSet, MovieLanguagesListAPIView, MomentsListAPIView,
                    FavoriteViewSet, FavoriteMovieViewSet, HistoryListAPIView, RatingViewSet,
                    RegisterView, CustomLoginView, LogoutView)


router = routers.SimpleRouter()
router.register('profile', UserProfileViewSet)
router.register('movie', MovieViewSet)
router.register('favorite', FavoriteViewSet)
router.register('favorite_movie', FavoriteMovieViewSet)
router.register('rating', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('movies/', MovieLanguagesListAPIView.as_view(), name='movies'),
    path('country/', CountryListAPIView.as_view(), name='country'),
    path('director/', DirectorListAPIView.as_view(), name='director'),
    path('actor/', ActorListAPIView.as_view(), name='actor'),
    path('genre/', GenreListAPIView.as_view(), name='genre'),
    path('moments/', MomentsListAPIView.as_view(), name='moments'),
    path('history/', HistoryListAPIView.as_view(), name='history'),
]
