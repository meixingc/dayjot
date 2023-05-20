from rest_framework import serializers
from .models import User, Entry, Water, Food, Exercise, Sleep, Weight

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'picture']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EntrySerializer(serializers.ModelSerializer):
    water = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()
    exercise = serializers.SerializerMethodField()
    sleep = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    class Meta:
        model = Entry
        fields = ['id', 'user', 'date', 'diary', 'water', 'food', 'exercise', 'sleep', 'weight']
    def get_water(self, obj):
        water = Water.objects.filter(entry=obj)
        return WaterSerializer(water, many=True).data
    def get_food(self, obj):
        food = Food.objects.filter(entry=obj)
        return FoodSerializer(food, many=True).data
    def get_exercise(self, obj):
        exercise = Exercise.objects.filter(entry=obj)
        return ExerciseSerializer(exercise, many=True).data
    def get_sleep(self, obj):
        sleep = Sleep.objects.filter(entry=obj)
        return SleepSerializer(sleep, many=True).data
    def get_weight(self, obj):
        weight = Weight.objects.filter(entry=obj)
        return WeightSerializer(weight, many=True).data

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ['id', 'entry', 'amount']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'entry', 'name', 'amount', 'calories']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'entry', 'name', 'duration', 'calories', 'links']

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ['id', 'entry', 'duration']

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['id', 'entry', 'weight']

        