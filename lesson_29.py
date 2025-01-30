"""
Тема: ООП Ч6. Миксины на примерах. Урок: 29
- Псевдокод Django и добавление MenuMixin в классы
"""


class View:
    """
    Класс имитирующий работу вью в Django
    """



class BlogModel:
    """
    Класс имитирующий работу БД в Джанго
    """

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'Пост "{self.title}" от {self.author}. {self.content[:20]}...'
    
    
    def __repr__(self):
        return f"{self.__class__.__name__}. {self.__dict__}"


class MenuMixin:
    """
    Миксин имитирующий добавление меню в классовые вью в Django
    """

    menu_data = [
        {"main": "Главная", "url": "/"},
        {"main": "О нас", "url": "/about"},
        {"main": "Контакты", "url": "/contacts"},
        {"main": "Блог", "url": "/blog"},
    ]

    def get_menu(self):
        return self.menu_data


class BlogListView(MenuMixin, View):
    """
    Имитация представления каталога постов в блоге
    """

    def __init__(self, posts: list[BlogModel]):
        self.posts = posts

    def __call__(self):
        print(self.get_menu())
        return self.posts


class BlogDetailView(MenuMixin, View):
    """
    Имитация представления детального отображения поста в блоге
    """

    def __init__(self, post: BlogModel):
        self.post = post

    def __call__(self):
        print(self.get_menu())
        return self.post


# ТЕСТИРУЕМ

# Создаем посты
posts = [
    BlogModel(
        "Django для новичков",
        "Очередной пост от маэстро Питоньи о том что Джанго может освоить каждый!",
        "Питонья",
    ),
    BlogModel(
        "Покружаемся в кроличью нору PostgreSQL",
        "Сегодня мы продолжим погружение в удивительный мир баз данных и открытой и свободной Постгры!",
        "Автор 2",
    ),
    BlogModel(
        "Флас",
        "Бегите глупцы! Он не так прост как его пытаются представить! Всё придется делать своими руками!!!!",
        "Анон",
    ),
]

# Создаем экземпляры вью
blog_list_view = BlogListView(posts)
blog_detail_view = BlogDetailView(posts[0])

# Делаем тест!
if __name__ == "__main__":
    print(blog_list_view())   # __repr__
    print("-" * 50)
    print(blog_detail_view())  # __str__
    print()
