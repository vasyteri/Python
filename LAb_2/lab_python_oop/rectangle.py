from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    """
    Класс "Прямоугольник", наследуется от Figure.
    """
    
    FIGURE_TYPE = "Прямоугольник" 

    def __init__(self, width_param, height_param, color_param):
        """
        Конструктор прямоугольника.
        :param width_param: Ширина.
        :param height_param: Высота.
        :param color_param: Цвет (строка).
        """
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor(color_param)

    def area(self):
        """
        Переопределенный метод для вычисления площади прямоугольника.
        """
        return self.width * self.height

    def __repr__(self):
        """
        Метод repr, возвращающий основные параметры фигуры, ее цвет и площадь.
        """
        return '"{}, ширина {}, высота {}, цвет {}, площадь {}"'.format(
            self.get_figure_type(),
            self.width,
            self.height,
            self.fc.color,
            self.area()
        )
        
    @classmethod
    def get_figure_type(cls):
        """
        Метод класса, возвращающий название фигуры.
        """
        return cls.FIGURE_TYPE