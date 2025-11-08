from .models import Country, Director, Actor, Movie, Rating, Genre, MovieLanguages
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio')

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(MovieLanguages)
class   MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('languages',)

@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('movie', 'text',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)