from rest_framework import serializers
from .models import (UserProfile, Country, Director, Actor, Genre,
                     Movie, MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountryListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['movie_image', 'movie_name', 'year', 'genre', 'country', 'status_movie', 'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class GenreDetailSerializer(serializers.ModelSerializer):
    movie_genre = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = ['genre_name', 'movie_genre']

class ActorDetailSerializer(serializers.ModelSerializer):
    movie_actor = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image', 'movie_actor']



class CountryDetailSerializer(serializers.ModelSerializer):
    movie_countries = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Country
        fields = ['country_name', 'movie_countries']

class DirectorDetailSerializer(serializers.ModelSerializer):
    movies_director = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age', 'director_image', 'movies_director']

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['languages', 'video']

class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')


    class Meta:
        model = Rating
        fields = ['id', 'parent_movie', 'user', 'stars', 'text', 'created_date']



class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    country = CountryListSerializer(many=True)
    director = DirectorListSerializer(many=True)
    actor = ActorListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    movie_frames = MomentsSerializer(many=True, read_only=True)
    movie_videos = MovieLanguagesSerializer(many=True, read_only=True)
    movie_ratings = RatingSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'description', 'director' ,'actor', 'genre', 'types',
                  'movie_time', 'movie_trailer', 'movie_image', 'status_movie', 'movie_frames', 'movie_videos', 'get_avg_rating', 'get_count_people','movie_ratings']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['favorite', 'movie']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']
