from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math

class Circle(Figure):
    """
    Класс "Круг", наследуется от Figure.
    """
    
    FIGURE_TYPE = "Круг" 

    def __init__(self, radius_param, color_param):
        """
        Конструктор круга.
        :param radius_param: Радиус.
        :param color_param: Цвет (строка).
        """
        self.radius = radius_param
        self.fc = FigureColor(color_param)

    def area(self):
        """
        Переопределенный метод для вычисления площади круга.
        """
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        """
        Метод repr, возвращающий основные параметры фигуры, ее цвет и площадь.
        """
        return '"{}, радиус {:.2f}, цвет {}, площадь {:.2f}"'.format(
            self.get_figure_type(),
            self.radius,
            self.fc.color,
            self.area()
        )

    @classmethod
    def get_figure_type(cls):
        """
        Метод класса, возвращающий название фигуры.
        """
        return cls.FIGURE_TYPE