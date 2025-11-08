from django.contrib import admin
from.models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class MovieLanguagesInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = MovieLanguages
    extra = 1

@admin.register(Movie)
class ProductAdmin(TranslationAdmin):
    inlines = [MovieLanguagesInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Country, Director, Actor, Rating, Genre)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Moments)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)


