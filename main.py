
'''Реализация функции, выводящая значения элементов односвязного списка(в данном случае словаря) в обратном порядке.
Рекурсивный обход словаря с добавлением значений в стек и последующим принтом. При использовании классов, можно ограничиться
передачей указателя на следующий элемент(head.next)'''



def reverse_print(some_list,stek=[]):
    for value in some_list.values():
        if isinstance(value, dict):
            reverse_print(value)
        elif isinstance(value, int):
            stek.append(value)
    while stek:
        print(stek.pop(),end=' ')


some_list = {
  'value': 1,
  'next': {
    'value': 2,
    'next': {
      'value': 3,
      'next': {
        'value': 4,
        'next': None,
      },
    },
  },
}


reverse_print(some_list)



