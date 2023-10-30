from modeltranslation.translator import TranslationOptions, register
from .models import HomeData, Slider, Features, SiteInformation, HelpfulLinks

@register(HomeData)
class HomeDataTranslationOptions(TranslationOptions):
    fields = ['title', 'about', 'mission', 'quote', 'sub_industries']

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(SiteInformation)
class SiteInformationTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'address']


@register(HelpfulLinks)
class HelpfulLinksTranslationOptions(TranslationOptions):
    fields = ['title',]