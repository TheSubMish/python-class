from rest_framework import serializers

from .models import TodoModel, StatusChoice


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    status = serializers.ChoiceField(
        choices=StatusChoice.choices, default=StatusChoice.PENDING
    )
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        print("Validating attributes:", attrs)
        return super().validate(attrs)

    def validate_title(self, value):

        print("Validating title:", value)

        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def create(self, validated_data):
        return TodoModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
