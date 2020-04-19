from rest_framework import serializers
from .models import Dog,  Kennel, DogBreed
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class DogBreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogBreed
        fields = ('id', 'name', 'desc', 'photo', "number", 'size', 'hair', 'country')
        read_only_fields = ('id',)


class KennelSerializer(serializers.ModelSerializer):
    breeds = DogBreedSerializer()

    class Meta:
        model = Kennel
        fields = ('name', 'about', 'photo', 'breeds', 'city')


class DogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'size', 'age', 'units', 'photo', 'hair',  'kennel', 'breed', 'sex')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'size', 'age', 'units', 'photo', 'hair', 'kennel', 'breed', 'sex')

    # def create(self, validated_data):
    #     breed_data = validated_data.pop('breed')
    #     dog = Dog.objects.create(**validated_data)
    #     DogBreed.objects.create(dog=dog, **breed_data)
    #     return dog



# class FCIGroupSerializer(serializers.ModelSerializer):
#     breeds = DogBreedSerializer()
#
#     class Meta:
#         model = FCIGroup
#         fields = ('name', 'number')



# class DogBreedSerializer(serializers.ModelSerializer):
#   class Meta:
#     Model = DogBreed
#     fields = ('name', 'desc')


# class DogBreedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DogBreed
#         fields = "__all__"
#
# class DogListSerializer(serializers.ModelSerializer):
#     hair = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     age = serializers.IntegerField(required=True)
#     units = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     photo = serializers.URLField(required=False)
#     size = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     units = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     breed = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     price = serializers.IntegerField(required=True)
#
#     class Meta:
#         model = Dog
#         fields = ('id', 'hair', 'age', 'units', 'photo', 'size', 'price', 'breed')
#
#
# class DogSerializer(serializers.ModelSerializer):
#     hair = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     age = serializers.IntegerField(required=True)
#     units = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     photo = serializers.URLField(required=False)
#     size = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     units = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     breed = serializers.CharField(max_length=50, allow_blank=True, required=False)
#     price = serializers.IntegerField(required=True)
#     description = serializers.CharField(max_length=1000, allow_blank=True, required=False)
#
#     class Meta:
#         model = Dog
#         fields = ('id', 'hair', 'age', 'units', 'photo', 'size', 'description','price','breed' )




