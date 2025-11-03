class Computer:
    """Класс Компьютер"""
    def __init__(self, id, model):
        self.id = id
        self.model = model

    def __repr__(self):
        return f"Computer(id={self.id}, model='{self.model}')"

class Browser:
    """Класс Браузер"""
    def __init__(self, id, name, memory_usage, computer_id):
        self.id = id
        self.name = name
        self.memory_usage = memory_usage  # количественный признак - использование памяти в МБ
        self.computer_id = computer_id

    def __repr__(self):
        return f"Browser(id={self.id}, name='{self.name}', memory_usage={self.memory_usage}, computer_id={self.computer_id})"

class BrowserComputer:
    """Класс для связи многие-ко-многим между Браузером и Компьютером"""
    def __init__(self, browser_id, computer_id):
        self.browser_id = browser_id
        self.computer_id = computer_id

    def __repr__(self):
        return f"BrowserComputer(browser_id={self.browser_id}, computer_id={self.computer_id})"

def main():
    # 2) Создание тестовых данных

    # Создаем компьютеры
    computers = [
        Computer(1, "Dell XPS 15"),
        Computer(2, "HP Pavilion"),
        Computer(3, "Lenovo ThinkPad"),
        Computer(4, "Asus ROG"),
        Computer(5, "Acer Aspire")
    ]

    # Создаем браузеры (связь один-ко-многим)
    browsers = [
        Browser(1, "Chrome", 450, 1),
        Browser(2, "Firefox", 320, 1),
        Browser(3, "Edge", 280, 2),
        Browser(4, "Safari", 350, 3),
        Browser(5, "Opera", 180, 3),
        Browser(6, "Chrome", 420, 4),
        Browser(7, "Firefox", 300, 5),
        Browser(8, "Иванов Браузер", 250, 2),  # Русское название с "ов"
        Browser(9, "Петров Навигатор", 190, 4),  # Русское название с "ов"
        Browser(10, "Сидоров Обозреватель", 220, 1),  # Русское название с "ов"
        Browser(11, "Google Chrome", 400, 2)
    ]

    # Создаем связи многие-ко-многим
    browser_computers = [
        BrowserComputer(1, 1),  # Chrome - Dell XPS 15
        BrowserComputer(2, 1),  # Firefox - Dell XPS 15
        BrowserComputer(3, 2),  # Edge - HP Pavilion
        BrowserComputer(4, 3),  # Safari - Lenovo ThinkPad
        BrowserComputer(5, 3),  # Opera - Lenovo ThinkPad
        BrowserComputer(6, 4),  # Chrome - Asus ROG
        BrowserComputer(7, 5),  # Firefox - Acer Aspire
        BrowserComputer(8, 2),  # Иванов Браузер - HP Pavilion
        BrowserComputer(9, 4),  # Петров Навигатор - Asus ROG
        BrowserComputer(10, 1), # Сидоров Обозреватель - Dell XPS 15
        BrowserComputer(11, 2), # Google Chrome - HP Pavilion
        # Дополнительные связи для демонстрации многие-ко-многим
        BrowserComputer(1, 2),  # Chrome также на HP Pavilion
        BrowserComputer(3, 1),  # Edge также на Dell XPS 15
        BrowserComputer(5, 4),  # Opera также на Asus ROG
        BrowserComputer(7, 3),  # Firefox также на Lenovo ThinkPad
    ]

    print("=" * 80)
    print("ТЕСТОВЫЕ ДАННЫЕ")
    print("=" * 80)

    print("\nКомпьютеры:")
    for comp in computers:
        print(f"  {comp}")

    print("\nБраузеры:")
    for browser in browsers:
        print(f"  {browser}")

    print("\nСвязи браузеры-компьютеры:")
    for bc in browser_computers:
        print(f"  {bc}")

    # 3) Выполнение запросов

    print("\n" + "=" * 80)
    print("ЗАПРОС №1")
    print("=" * 80)
    print("Список всех браузеров, у которых название заканчивается на «ов», ")
    print("и названия компьютеров, на которых они установлены:")

    # Запрос 1: Браузеры с  названиями, заканчивающимися на "ов"
    def has_russian_ov_ending(name):
        words = name.split()
        for word in words:
                if word.lower().endswith('ов'):
                    return True
        return False

    browsers_with_ov = [browser for browser in browsers if has_russian_ov_ending(browser.name)]

    for browser in browsers_with_ov:
        computer = next((comp for comp in computers if comp.id == browser.computer_id), None)
        if computer:
            print(f"Браузер: '{browser.name}', Компьютер: '{computer.model}'")
        else:
            print(f"Браузер: '{browser.name}', Компьютер: не найден")

    print("\n" + "=" * 80)
    print("ЗАПРОС №2")
    print("=" * 80)
    print("Список компьютеров со средней нагрузкой памяти браузеров")
    print("на каждом компьютере, отсортированный по средней нагрузке:")

    # Запрос 2: Компьютеры со средней нагрузкой памяти, отсортированные по нагрузке
    from collections import defaultdict

    # Группируем браузеры по компьютерам
    browsers_by_computer = defaultdict(list)
    for browser in browsers:
        browsers_by_computer[browser.computer_id].append(browser)

    # Вычисляем среднюю нагрузку памяти для каждого компьютера
    computer_avg_memory = []
    for comp_id, comp_browsers in browsers_by_computer.items():
        if comp_browsers:
            total_memory = sum(browser.memory_usage for browser in comp_browsers)
            avg_memory = total_memory / len(comp_browsers)
            comp_model = next(comp.model for comp in computers if comp.id == comp_id)
            computer_avg_memory.append((comp_model, avg_memory))

    # Сортируем по средней нагрузке памяти (по возрастанию)
    computer_avg_memory.sort(key=lambda x: x[1])

    for comp_model, avg_memory in computer_avg_memory:
        print(f"Компьютер '{comp_model}': средняя нагрузка памяти = {avg_memory:.2f} МБ")

    print("\n" + "=" * 80)
    print("ЗАПРОС №3")
    print("=" * 80)
    print("Список всех компьютеров, у которых модель начинается с буквы «А», ")
    print("и список браузеров, установленных на них (многие-ко-многим):")

    # Запрос 3: Компьютеры на "А" и их браузеры (многие-ко-многим)
    browser_dict = {browser.id: browser for browser in browsers}
    computer_dict = {comp.id: comp for comp in computers}

    # Группируем связи по компьютерам
    connections_by_computer = defaultdict(list)
    for bc in browser_computers:
        browser = browser_dict.get(bc.browser_id)
        computer = computer_dict.get(bc.computer_id)
        if browser and computer:
            connections_by_computer[computer].append(browser)

    # Фильтруем компьютеры, начинающиеся на "А"
    computers_with_a = [comp for comp in connections_by_computer.keys() if comp.model.startswith('A')]

    # Сортируем компьютеры по названию модели
    sorted_computers = sorted(computers_with_a, key=lambda x: x.model)

    for computer in sorted_computers:
        computer_browsers = connections_by_computer[computer]
        print(f"\nКомпьютер: {computer.model}")
        for browser in computer_browsers:
            print(f"  - Браузер '{browser.name}' (память: {browser.memory_usage} МБ)")

if __name__ == "__main__":
    main()