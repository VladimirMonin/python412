"""
Тема ООП Ч10. Паттерны ООП. Урок: 33
- Абстрактная фабрика
- Фасад
- Прототип
- Декоратор
- Посредник (Proxy)
- Адаптер (Apapter)
- Мост (Bridge)
"""

from abc import ABC, abstractmethod


# Интерфейс реализации графического API
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x, y, radius):
        pass


class OpenGLRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"Рендер OpenGL: круг с центром ({x},{y}) и радиусом {radius}")


class DirectXRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"Рендер DirectX: круг с центром ({x},{y}) и радиусом {radius}")


# Абстракция
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, x, y, radius):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.x, self.y, self.radius)


# Использование
if __name__ == "__main__":
    opengl = OpenGLRenderer()
    directx = DirectXRenderer()

    # Рисуем круг с использованием OpenGL
    circle1 = Circle(opengl, 10, 20, 15)
    circle1.draw()

    # Рисуем круг с использованием DirectX
    circle2 = Circle(directx, 30, 40, 25)
    circle2.draw()
