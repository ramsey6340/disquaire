from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from shop.models import Category, Product, Article
from shop.serializers import CategoryDetailSerializer, CategoryListSerializer, ProductDetailSerializer, \
    ProductListSerializer, ArticleDetailSerializer, ArticleListSerializer
from rest_framework.decorators import action


class AdminCategoryViewSet(ModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class AdminArticleViewSet(ModelViewSet):
    serializer_class = ArticleListSerializer
    detail_serializer_class = ArticleDetailSerializer

    def get_queryset(self):
        return Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class

        return super().get_serializer_class()


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(methods=['post'], detail=True)
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

    @action(methods=['post'], detail=True)
    def enable(self, request, pk):
        self.get_object().enable()
        return Response()


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category=category_id)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(methods=['post'], detail=True)
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

    @action(methods=['post'], detail=True)
    def enable(self, request, pk):
        self.get_object().enable()
        return Response()


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleListSerializer
    detail_serializer_class = ArticleDetailSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product=product_id)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(methods=['post'], detail=True)
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

    @action(methods=['post'], detail=True)
    def enable(self, request, pk):
        self.get_object().enable()
        return Response()
