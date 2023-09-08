from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from shop.models import Category, Product, Article


class ArticleListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'description', 'active']

    def validate_price(self, value):
        if value <= 1:
            raise ValidationError('Le prix est trop faible')
        return value

    def validate_product(self, value):
        if value.active is False:
            raise ValidationError('Le produit correspondant est desactiver. Activer puis réessayer')
        return value


class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'active', 'product']


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name']


class ProductDetailSerializer(ModelSerializer):
    articles = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'category', 'active', 'articles']

    def get_articles(self, product):
        queryset = product.articles.filter(active=True)
        serializer = ArticleListSerializer(queryset, many=True)
        return serializer.data


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise ValidationError('La catégorie existe déjà')
        return value

    def validate(self, data):
        if data['name'] not in data['description']:
            raise ValidationError('La description doit contenir le nom du produit')
        return data


class CategoryDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description', 'active', 'products']

    def get_products(self, category):
        queryset = category.products.filter(active=True)
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data

