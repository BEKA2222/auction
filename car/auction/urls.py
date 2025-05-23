from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'carmodels', CarModelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]