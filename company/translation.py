from modeltranslation.translator import TranslationOptions, register
from .models import Company

@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']