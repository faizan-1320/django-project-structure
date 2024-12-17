from rest_framework import serializers
from .models import TOdo

class ToDoCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    is_completed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        title = validated_data.get('title')
        description = validated_data.get('description')
        due_date = validated_data.get('due_date')
        todo_create = TOdo.objects.create(title=title,description=description,due_date=due_date,user=user)
        return todo_create
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance

