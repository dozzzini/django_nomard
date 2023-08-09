from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    # read_only=True를 해주는 이유는 pk와 created_at은 사용자가 보내는 정보가 아니라는 것을 알려주기 위함임.
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):  # CategorySerializer내에 있는 유효한 data
        print(validated_data)
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
