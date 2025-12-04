from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests 
import sys
import math


N = 18 
print(f"Используем N = {N} ( номер варианта).")

def main():
    # 1. Прямоугольник синего цвета шириной N и высотой N.
    rect = Rectangle(N, N, "синий")
    print(repr(rect))

    # 2. Круг зеленого цвета радиусом N.
    circ = Circle(N, "зеленый")
    print(repr(circ))

    # 3. Квадрат красного цвета со стороной N.
    sq = Square(N, "красный")
    print(repr(sq))
    
    print("\n--- Вызов метода внешнего пакета (requests) ---")
    
    try:

        response = requests.get('https://www.google.com/', timeout=5)
        
        print(f"Запрос к Google.com успешен. Статус-код: {response.status_code}")
        print(f"Тип контента: {response.headers.get('Content-Type', 'Не указан')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        
    print("-------------------------------------------------")
    
    print(f"Версия Python: {sys.version.split()[0]}")
    print(f"Значение math.pi: {math.pi}")

if __name__ == "__main__":
    main()