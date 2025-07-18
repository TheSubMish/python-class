from rest_framework import serializers


from .models import TodoModel


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoModel
        fields = "__all__"


# user - subodh mishra

def get_user(self):
    return f"user.first_name user.last_name"


class TodoReadSeraializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = TodoModel
        fields = ["id", "title", "status", "created_at", "updated_at","custom_field"]

    def validate_title(self, attrs):
        return super().validate(attrs)

    def get_custom_field(self, obj):
        return f"Custom Field: {obj.title} - {obj.status}"
