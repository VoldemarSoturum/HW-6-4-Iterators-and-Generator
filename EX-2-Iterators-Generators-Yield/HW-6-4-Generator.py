
# ЗАДАЧА2:


#     Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.

# import types


# def flat_generator(list_of_lists):

#     ...
#     yield
#     ...


# def test_2():

#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]

#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):

#         assert flat_iterator_item == check_item

#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


# if __name__ == '__main__':
#     test_2()
    

# ОТВЕТ:
# Импортируем модуль types для проверки типа генератора
import types


# Функция-генератор, которая делает плоское представление списка списков
def flat_generator(list_of_lists):
    # Внешний цикл: перебираем каждый подсписок в основном списке
    for sublist in list_of_lists:
        # Внутренний цикл: перебираем каждый элемент в текущем подсписке
        for item in sublist:
            # Приостанавливаем выполнение функции и возвращаем текущий элемент
            # При следующем вызове выполнение продолжится с этого места
            yield item


# Функция для тестирования генератора
def test_2():
    # Тестовые данные - список списков с разными типами элементов
    list_of_lists_1 = [
        ['a', 'b', 'c'],              # Подсписок из строк
        ['d', 'e', 'f', 'h', False],   # Подсписок из строк и булева значения
        [1, 2, None]                   # Подсписок из чисел и None
    ]

    # Тестируем генератор с помощью zip:
    # flat_generator создает плоскую последовательность,
    # второй аргумент - ожидаемый результат
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),  # Создаем генератор
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]  # Эталон
    ):
        # Проверяем, что элементы совпадают
        assert flat_iterator_item == check_item

    # Проверяем, что генератор полностью преобразуется в правильный список
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Проверяем, что flat_generator действительно возвращает генератор
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    
    # ДЛЯ НАГЛЯДНОСТИ РЕЗУЛЬТАТ В СПИСОК
    result_list = list(flat_generator(list_of_lists_1))
    print("Результат как список:", result_list)

# Если скрипт запущен напрямую (а не импортирован как модуль)
if __name__ == '__main__':
    # Запускаем тестирование
    test_2()
    
# Генератор работает только один раз, так как при каждом вызове 
# он продолжает с того места, где был остановлен.
