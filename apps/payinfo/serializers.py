from rest_framework import serializers
from .models import PayInfo


class PayInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayInfo
        fields = "__all__"




