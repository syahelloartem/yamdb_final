from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category, Genre, Title, Comment, Review, GenreTitle
from users.models import User


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        for row in DictReader(
                open('./static/data/category.csv', encoding='UTF-8')
        ):
            Category(id=row['id'], name=row['name'], slug=row['slug']).save()

        for row in DictReader(open(
                './static/data/genre.csv',
                encoding='UTF-8'
        )):
            Genre(id=row['id'], name=row['name'], slug=row['slug']).save()

        for row in DictReader(open(
                './static/data/titles.csv',
                encoding='UTF-8'
        )):
            Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            ).save()

        for row in DictReader(open(
                './static/data/genre_title.csv',
                encoding='UTF-8'
        )):
            GenreTitle(
                id=row['id'],
                title_id=row['title_id'],
                genre_id=row['genre_id']
            ).save()

        for row in DictReader(open(
                './static/data/users.csv',
                encoding='UTF-8'
        )):
            User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            ).save()

        for row in DictReader(open(
                './static/data/review.csv',
                encoding='UTF-8'
        )):
            Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            ).save()

        for row in DictReader(open(
                './static/data/comments.csv',
                encoding='UTF-8'
        )):
            Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            ).save()
