from django.core.management.base import BaseCommand
from blogapp.models import Category, Post


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории
        categories = Category.objects.all()
        # Выводим результат в виде QuerySet - это аналог списка
        print(categories)
        print(type(categories))
        # В цикле идем по всем елементам и выводим их,их тип и  их значение
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))
        print('End')

        # Первый пост
        post = Post.objects.first()
        # Выведем его имя
        print(post.name)
        print(post.text)

        # Получим категорию связанную с постом
        # ForeignKey
        category = post.category
        # Выведем её имя и тип
        print(category.name)
        print(type(category))

        # Создание
        Category.objects.create(name='Новая', description='Что то')
        print('Создали')

        # Изменение
        category = Category.objects.get(name='Новая')
        category.name = 'Измененная'
        category.save()
        print('Изменили')

        # Удаление
        # Можно одну,
        category.delete()
        print('Удалили')
        # можно несколько
        # Category.objects.all().delete()
        # Проверяем что всё удалилось
        categories = Category.objects.all()
        # Выводим результат в виде QuerySet - это аналог списка
        print(categories)


