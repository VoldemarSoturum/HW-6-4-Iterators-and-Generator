#ЗАДАНИЕ:
# 3.* Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

# class FlatIterator:

#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list

#     def __iter__(self):
#         ...
#         return self
    
#     def __next__(self):
#         ...
#         return item


# def test_3():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# if __name__ == '__main__':
#     test_3()

#ОТВЕТ:
class FlatIterator:
    # Класс итератора для обработки списков с любой вложенностью

    def __init__(self, list_of_list):
        # Инициализация итератора
        self.list_of_list = list_of_list  # Сохраняем исходный список
        self.stack = [iter(list_of_list)]  # Стек для хранения итераторов всех уровней
        self.current_iter = None  # Текущий активный итератор

    def __iter__(self):
        # Метод, возвращающий сам итератор (для поддержки протокола итерации)
        self.stack = [iter(self.list_of_list)]  # Инициализируем стек корневым итератором
        self.current_iter = None  # Сбрасываем текущий итератор
        return self  # Возвращаем сам объект итератора
    
    def __next__(self):
        # Основной метод получения следующего элемента
        while self.stack:  # Пока в стеке есть итераторы
            try:
                if self.current_iter is None:  # Если текущий итератор не установлен
                    self.current_iter = self.stack[-1]  # Берем последний из стека
                
                item = next(self.current_iter)  # Пробуем получить следующий элемент
                
                if isinstance(item, list):  # Если элемент - список
                    self.stack.append(iter(item))  # Добавляем его итератор в стек
                    self.current_iter = None  # Сбрасываем текущий итератор
                else:
                    return item  # Возвращаем обычный элемент
            except StopIteration:  # Если текущий итератор закончился
                self.stack.pop()  # Удаляем его из стека
                self.current_iter = None  # Сбрасываем текущий итератор
                continue  # Продолжаем цикл
        
        raise StopIteration  # Если стек пуст - завершаем итерацию


def test_3():
    # Тестовая функция для проверки работы итератора
    
    # Сложный вложенный список для тестирования
    list_of_lists_2 = [
        [['a'], ['b', 'c']],  # Уровень вложенности 2
        ['d', 'e', [['f'], 'h'], False],  # Разная вложенность
        [1, 2, None, [[[[['!']]]]], []]  # Глубокая вложенность + пустой список
    ]

    # Проверка соответствия элементов через zip
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),  # Наш итератор
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']  # Ожидаемый результат
    ):
        assert flat_iterator_item == check_item  # Проверка каждого элемента

    # Проверка полного преобразования в список
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    
    # НАГЛЯДНЫЫЙ ВЫВОД С НУМЕРАЦИЕЙ ЭЛЕМЕНТА ПОСЛЕ ВЫРАВНИВАНИЯ В ПЛОСКИЙ СПИСОК
    print("\nВывод с нумерацией:")
    for i, item in enumerate(FlatIterator(list_of_lists_2), 1):  # Нумерация с 1
        print(f"{i}. {item}")  # Форматированный вывод

if __name__ == '__main__':
    test_3()  # Запуск тестов при непосредственном выполнении скрипта