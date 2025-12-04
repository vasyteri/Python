from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """
    Класс "Квадрат", наследуется от Rectangle.
    """
    
    FIGURE_TYPE = "Квадрат" 

    def __init__(self, side_param, color_param):
        """
        Конструктор квадрата.
        :param side_param: Длина стороны.
        :param color_param: Цвет (строка).
        """
        super().__init__(side_param, side_param, color_param)
        self.side = side_param 

    def __repr__(self):
        """
        Переопределенный метод repr для квадрата.
        """
        return '"{}, сторона {}, цвет {}, площадь {}"'.format(
            self.get_figure_type(),
            self.side,
            self.fc.color,
            self.area()
        )