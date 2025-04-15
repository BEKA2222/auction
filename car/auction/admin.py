from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Brand, CarModel, Car, Auction, Bid, Feedback


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarInline(admin.TabularInline):
    model = Car
    extra = 1
    raw_id_fields = ('brand', 'car_model', 'seller')

class AuctionInline(admin.TabularInline):
    model = Auction
    extra = 1
    raw_id_fields = ('car',)

class BidInline(admin.TabularInline):
    model = Bid
    extra = 1
    raw_id_fields = ('auction', 'buyer')

class FeedbackAsSellerInline(admin.TabularInline):
    model = Feedback
    extra = 1
    fk_name = 'seller'
    raw_id_fields = ('buyer',)

class FeedbackAsBuyerInline(admin.TabularInline):
    model = Feedback
    extra = 1
    fk_name = 'buyer'
    raw_id_fields = ('seller',)



class UserProfileAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone_number', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'role', 'password1', 'password2'),
        }),
    )
    inlines = [CarInline, BidInline, FeedbackAsSellerInline, FeedbackAsBuyerInline]
    ordering = ('username',)



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name')
    search_fields = ('brand_name',)
    inlines = [CarModelInline, CarInline]
    ordering = ('brand_name',)



@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_model', 'brand')
    list_filter = ('brand',)
    search_fields = ('car_model', 'brand__brand_name')
    inlines = [CarInline]
    ordering = ('car_model',)



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'car_model', 'year', 'fuel_type', 'transmission', 'mileage', 'price', 'seller')
    list_filter = ('brand', 'car_model', 'year', 'fuel_type', 'transmission', 'seller')  # Исправлено: закрыты кавычки и кортеж
    search_fields = ('description', 'brand__brand_name', 'car_model__car_model', 'seller__username')
    inlines = [AuctionInline]
    list_editable = ('price', 'year', 'mileage')
    ordering = ('-id',)
    raw_id_fields = ('brand', 'car_model', 'seller')



@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'start_price', 'min_price', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'start_time', 'end_time')
    search_fields = ('car__brand__brand_name', 'car__car_model__car_model')
    inlines = [BidInline]
    list_editable = ('status', 'start_price', 'min_price')
    ordering = ('-start_time',)
    raw_id_fields = ('car',)



@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'auction', 'buyer', 'amount', 'created_at')
    list_filter = ('auction', 'buyer', 'created_at')
    search_fields = ('auction__car__brand__brand_name', 'buyer__username')
    ordering = ('-created_at',)
    raw_id_fields = ('auction', 'buyer')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'buyer', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('seller__username', 'buyer__username', 'comment')
    ordering = ('-created_at',)
    raw_id_fields = ('seller', 'buyer')
    list_editable = ('rating',)


admin.site.register(UserProfile, UserProfileAdmin)