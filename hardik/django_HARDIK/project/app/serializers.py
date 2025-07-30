from rest_framework import serializers

from .models import Note,Status

class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)
    status = serializers.ChoiceField(
        choices=Status.choices,
        default = Status.PENDING
        )
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.content = validated_data.get("content",instance.content)
        instance.status = validated_data.get("status",instance.status)
        instance.save()
        return instance
        
    