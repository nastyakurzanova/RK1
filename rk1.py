from operator import itemgetter


class OS:
    """ОC"""

    def __init__(self, id, interface, price, name, computer_id):
        self.id = id
        self.interface = interface
        self.price = price
        self.name = name
        self.computer_id = computer_id


class Computer:
    """Компьютер"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class OSComputer:
    """ОC - Компьютер"""

    def __init__(self, computer_id, os_id):
        self.computer_id = computer_id
        self.os_id = os_id


"""id компьютера и его имя"""
computers = [
    Computer(1, 'PC-007'),
    Computer(2, '2Comp WS-01'),
    Computer(3, 'Admin-PS'),
    Computer(4, '4Comp_CU15OQA'),
    Computer(5, 'A58CS25AD'),
    Computer(6, '6Comp CS25'),
]

"""id ОС, тип интерфейса, цена, имя ОС,id компьютера"""
OSs = [
    OS(1, 'Графический', 0, 'linux', 1),
    OS(2, 'Текстовый', 0, 'Dos', 2),
    OS(3, 'Графический', 12000, 'Windows10', 3),
    OS(4, 'Командная строка', 0, 'Unix', 4),
    OS(5, 'Графический', 150000, 'MacOS', 5),
    OS(6, 'Графический', 19000, 'Windows10professional', 5),
    OS(7, 'Графический', 8000, 'Windows7', 1),
    OS(8, 'Текстовый', 0, 'Dos', 2),
]

"""id компьютера, id ОС"""
OSs_computers = [
    OSComputer(1, 1),
    OSComputer(2, 2),
    OSComputer(3, 3),
    OSComputer(4, 4),
    OSComputer(5, 5),
    OSComputer(5, 6),
    OSComputer(1, 7),
    OSComputer(2, 7),
    OSComputer(6, 3),
]


def main():
    one_to_many = [(o.name, c.name, o.interface, o.price)
                   for c in computers
                   for o in OSs
                   if o.computer_id == c.id]

    '''«Компьютер» и «Отдел» связаны соотношением один-ко-многим. Выведите список всех связанных ОС и 
    компьютеров, отсортированный по цене ОС, сортировка по компьютерам произвольная. '''

    print('Задание A1')
    res_a1 = sorted(one_to_many, key=itemgetter(1))
    print(res_a1)

    '''«Отдел» и «Сотрудник» связаны соотношением один-ко-многим. 
    Выведите список отделов с суммарной зарплатой сотрудников в каждом отделе, отсортированный по суммарной зарплате.'''

    print('Задание A2')
    res2 = []
    for i in computers:
        c_os = [_ for _ in filter(lambda a: a[1] == i.name, one_to_many)]
        if len(c_os) > 0:
            # sum цена
            sum_price = sum([_[3] for _ in c_os])
        res2.append((i.name, sum_price))
        res_a2 = sorted(res2, key=itemgetter(1), reverse=True)
    print(res_a2)

    '''«Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите список всех отделов, у которых в 
    названии присутствует слово «отдел», и список работающих в них сотрудников. '''

    print('Задание A3')
    res_a3 = []
    for i in OSs_computers:
        os_for_comp = []
        if 'Comp' in computers[i.computer_id - 1].name:
            # many_to_many
            for j in OSs_computers:
                if computers[i.computer_id - 1].name == computers[j.computer_id - 1].name:
                    os_for_comp.append(OSs[j.os_id - 1].name)
            if (computers[i.computer_id - 1].name, os_for_comp) not in res_a3:
                res_a3.append((computers[i.computer_id - 1].name, os_for_comp))
    print(res_a3)


if __name__ == '__main__':
    main()
