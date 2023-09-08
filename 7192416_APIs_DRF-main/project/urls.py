from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from shop.views import CategoryViewSet, ProductViewSet, ArticleViewSet, AdminCategoryViewSet, AdminArticleViewSet
from rest_framework import routers

# Création d'une instance de route
router = routers.SimpleRouter()

# Enregistrement des URLs
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')
router.register('articles', ArticleViewSet, basename='articles')
router.register('admin/categories', AdminCategoryViewSet, basename='admin-category')
router.register('admin/articles', AdminArticleViewSet, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
