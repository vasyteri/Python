class FigureColor:
    """
    Класс, содержащий свойство для описания цвета геометрической фигуры.
    """
    def __init__(self, color_param):
        self._color = color_param

    @property
    def color(self):
        """Свойство для получения цвета."""
        return self._color

    @color.setter
    def color(self, value):
        """Свойство для установки цвета."""
        self._color = value