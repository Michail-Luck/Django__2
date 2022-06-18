from django.core.management.base import BaseCommand
from blogapp.models import Category, Post


# from blogapp.models import Poll

class Command(BaseCommand):


    def handle(self, *args, **options):
        # Выбираем ВСЕ категории и посты
        categories = Category.objects.all()
        posts = Post.objects.all()
        # Выводим статистику  по постам и категориям
        print('Количество категорий ', len(categories))
        print('Категории ', [ i.name for i in categories])
        print('Количество постов ', len(posts))
        print('Посты ', [i.name for i in posts])
        print('---'*10)
        # Читаем из файла данные
        with open('blogapp/static/Category.csv', 'r', encoding = 'utf8' ) as file:
            new_category = file.read().split('\n')
        # Создаем из данных новую категорию
        for cat in new_category:
            n_cat = cat.split(',')
            if len(n_cat)==2 and n_cat[0] not in [ i.name for i in categories]:
                Category.objects.create(name=n_cat[0], description=n_cat[1])
                print('Создали категорию')
        # Читаем из файла данные
        with open('blogapp/static/Post.csv', 'r', encoding = 'utf8' ) as file:
            new_post = file.read().split('\n')
        # Создаем из данных новые посты
        for pos in new_post:
            n_pos = pos.split(',')
            if len(n_pos) == 3 and n_pos[0] not in [i.name for i in posts]:
                if n_pos[2].strip() in [ i.name for i in categories]:
                    cat = Category.objects.get(name=n_pos[2].strip())
                    Post.objects.create(name=n_pos[0], text=n_pos[1], category=cat)
                    print('Создали пост')

        # Выбираем опять ВСЕ категории и посты
        categories = Category.objects.all()
        posts = Post.objects.all()
        # Выводим статистику  по постам и категориям
        print('---' * 10)
        print('Количество категорий ', len(categories))
        print('Категории ', [i.name for i in categories])
        print('Количество постов ', len(posts))
        print('Посты ', [i.name for i in posts])
        print('---' * 10)

