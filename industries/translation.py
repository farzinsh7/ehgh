from modeltranslation.translator import TranslationOptions, register
from .models import Industry

@register(Industry)
class IndustryTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']