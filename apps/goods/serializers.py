from rest_framework import serializers
from .models import Goods, GoodsCarousel


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class GoodsCarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCarousel
        fields = "__all__"


