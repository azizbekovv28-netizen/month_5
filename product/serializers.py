from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.product_set.count()
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_rating(self, obj):
        reviews = obj.reviews.all()

        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 2)

        return 0

