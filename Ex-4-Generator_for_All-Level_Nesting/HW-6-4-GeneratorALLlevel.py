# ЗАДАЧА:

# 4.* Необязательное задание. Написать генератор, аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

# import types


# def flat_generator(list_of_list):
#     ...
#     yield
#     ...

# def test_4():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

#     assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


# if __name__ == '__main__':
#     test_4()

#ОТВЕТ:
import types

def flat_generator(list_of_list):
    stack = list_of_list[::-1]  # Помещаем элементы в стек в обратном порядке
    
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])  # Добавляем элементы вложенного списка в обратном порядке
        else:
            yield item

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    # Проверка последовательности элементов
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    # Проверка полного преобразования
    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    # Проверка типа возвращаемого значения
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    # Дополнительный вывод для наглядности
    print("\nРезультат работы генератора (без рекурсии):")
    for i, item in enumerate(flat_generator(list_of_lists_2), 1):
        print(f"{i}. {item}")

if __name__ == '__main__':
    test_4()