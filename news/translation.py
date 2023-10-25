from modeltranslation.translator import TranslationOptions, register
from .models import News, Category, Tags

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ['title']