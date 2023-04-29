import datetime as dt

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Title, Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Category.objects.all())],
        max_length=256,
        required=True
    )
    slug = serializers.SlugField(
        validators=[UniqueValidator(queryset=Category.objects.all())],
        max_length=50,
        required=True
    )

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=256,
    )
    slug = serializers.SlugField(
        validators=[UniqueValidator(queryset=Genre.objects.all())],
        max_length=50,
        required=True
    )

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitlePostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=256,
        required=True,
    )
    year = serializers.IntegerField(
        required=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        required=True,
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        required=True,
        slug_field='slug',
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title

    def validate_year(self, value):
        current_year = dt.date.today().year
        if current_year < value:
            raise serializers.ValidationError('Проверьте год выпуска фильма!')
        return value


class TitleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True,
    )
    genre = GenreSerializer(
        many=True,
        read_only=True,
    )
    rating = serializers.IntegerField(
        read_only=True,
    )

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating',
            'description', 'genre', 'category'
        )
        model = Title
