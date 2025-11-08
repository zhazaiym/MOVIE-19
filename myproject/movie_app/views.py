from allauth.account.internal.userkit import user_display
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (UserProfile, Country, Director, Actor, Genre,Movie,Rating,Favorite,FavoriteMovie,History,MovieLanguages,Moments)
from .serializers import (UserProfileSerializer, CountryListSerializer, CountryDetailSerializer,
                          MovieListSerializer, MovieDetailSerializer,
                          DirectorListSerializer, DirectorDetailSerializer,
                          ActorListSerializer, ActorDetailSerializer, FavoriteSerializer,
                          MovieLanguagesSerializer,HistorySerializer,
                          GenreListSerializer, GenreDetailSerializer, RatingSerializer, MomentsSerializer, FavoriteMovieSerializer,
                          UserSerializer, LoginSerializer, )

from .filter import MovieFilter
from .pagination import MovieSetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from tokenize import TokenError
from .permission import CheckStatus, RatingPermission


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id = self.request.user.id)

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MovieSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]





class MovieDetailAPIView(generics.RetrieveAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieDetailSerializer
        permission_classes = [CheckStatus]




class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer


class HistoryListAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [RatingPermission]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer

class MovieLanguagesListAPIView(generics.ListAPIView):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer


class MomentsListAPIView(generics.ListAPIView):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer
