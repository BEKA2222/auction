from modeltranslation.translator import register, TranslationOptions
from .models import UserProfile, Brand, CarModel, Car, Auction, Bid, Feedback

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand_name',)

@register(CarModel)
class CarModelTranslationOptions(TranslationOptions):
    fields = ('car_model',)

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)