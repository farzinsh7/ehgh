from modeltranslation.translator import TranslationOptions, register
from .models import AboutCompany

@register(AboutCompany)
class AboutTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']