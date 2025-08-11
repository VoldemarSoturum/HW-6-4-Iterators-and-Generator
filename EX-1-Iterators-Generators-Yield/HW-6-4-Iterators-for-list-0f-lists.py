# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, 
# который принимает список списков и возвращает их плоское представление, т. е. 
# последовательность, состоящую из вложенных элементов. Функция test в коде ниже 
# также должна отработать без ошибок.

# Пример:
# class FlatIterator:

#     def __init__(self, list_of_list):
#         ...

#     def __iter__(self):
#         ...
#         return self

#     def __next__(self):
#         ...
#         return item


# def test_1():

#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# if __name__ == '__main__':
#     test_1()

# ОТВЕТ:
# Доработанный класс FlatIterator, который принимает список 
# списков и возвращает их плоское представление.
# ============================================

class FlatIterator:
    # Класс итератора для плоского представления списка списков

    def __init__(self, list_of_list):
        # Инициализация итератора
        self.list_of_list = list_of_list  # Сохраняем входной список списков
        self.current_list_index = 0        # Индекс текущего подсписка (внешний индекс)
        self.current_element_index = 0    # Индекс элемента в текущем подсписке (внутренний индекс)

    def __iter__(self):
        # Метод, возвращающий сам итератор (обязательный для итераторов)
        self.current_list_index = 0       # Сбрасываем внешний индекс при новом проходе
        self.current_element_index = 0    # Сбрасываем внутренний индекс при новом проходе
        return self                       # Возвращаем сам объект итератора

    def __next__(self):
        # Метод, возвращающий следующий элемент (обязательный для итераторов)
        
        # Проверяем, вышли ли за пределы списка списков
        if self.current_list_index >= len(self.list_of_list):
            raise StopIteration  # Если да - завершаем итерацию
        
        # Получаем текущий подсписок по внешнему индексу
        current_list = self.list_of_list[self.current_list_index]
        
        # Проверяем, вышли ли за пределы текущего подсписка
        if self.current_element_index >= len(current_list):
            self.current_list_index += 1    # Переходим к следующему подсписку
            self.current_element_index = 0  # Сбрасываем внутренний индекс
            return self.__next__()          # Рекурсивно вызываем себя для обработки перехода
        
        # Получаем текущий элемент
        item = current_list[self.current_element_index]
        self.current_element_index += 1  # Увеличиваем внутренний индекс для следующего вызова
        return item                     # Возвращаем текущий элемент


def test_1():
    # Тестовая функция для проверки работы итератора
    
    # Тестовые данные - список списков разной длины с разными типами элементов
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Проверяем последовательность элементов через zip
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),  # Создаем итератор
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]  # Ожидаемая последовательность
    ):
        # Проверяем соответствие каждого элемента
        assert flat_iterator_item == check_item

    # Проверяем полное преобразование в список
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

#ДЛЯ НАГЛЯДНОСТИ РАБОТЫ ИТЕРАТОРА!!!
    # Получаем результат работы итератора
    flat_list = list(FlatIterator(list_of_lists_1))
    
    # Выводим результат
    print("Результат работы FlatIterator:")
    print(flat_list)
    
    # Проверяем соответствие ожидаемому результату
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("\nОжидаемый результат:")
    print(expected)

if __name__ == '__main__':
    # Запуск теста при непосредственном выполнении скрипта
    test_1()