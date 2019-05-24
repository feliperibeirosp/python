# coding: utf-8


from decimal import Decimal


total = Decimal('0')
schema = ('NumDocumento', 'ValContrato')
_100M = Decimal('100000000')


def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal('0')

"""
with open('data/data/ExecucaoFinanceira.csv','r') as data:
    splited_data = [line.split(';') for line in data]
    total = sum([dec(element, 5) for element in splited_data])
    
print("Total gasto: {}".format(total))
"""
#
#
# with open('data/data/ExecucaoFinanceira.csv','r') as data_file:
#     splited_data = [line.split(';') for line in data_file]
#     data = [(element[2], dec(element, 12)) for element in
#             splited_data if len(element) > 2]
#     result = [{key:value for key, value in zip(schema, element)}
#               for element in data]
#
#     for info_dict in result:
#         print("{}".format(info_dict))

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    splited_data = [line.split(';') for line in data]
    values = [dec(element, 5) for element in splited_data]
    total = sum(values)
    values_100M = filter(lambda x: x > _100M, values)
    total_gt_100M = sum(values_100M)

percent = lambda x, y: (x/y) * Decimal('100')

print("Total gastos: {}".format(total))

print("Apenas contratos com mais de 100MI: {}", format(total_gt_100M))

print("Representam {:.2f}% do total".format(percent(total_gt_100M, total)))


class QueryFile():
    def __init__(self, filename):
        self._file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        data = self._file.readline().split(';')
        if not data or len(data) == 1:
            self._file.close()
            raise StopIteration

        returned_el = []
        for position in self.positions:
            if len(data) >= position:
                returned_el.append(data[position])

        return returned_el

    def __call__(self, *args):
        self.positions = args
        return self


query = QueryFile('data/data/ExecucaoFinanceira.csv')
"""
for data in query(5, 7):
    print("Execucao no valor de {} assinada {}".format(data[0], data[1]))

total = sum(dec(element, 5) for element in query)

print("Total gasto: {}".format(total))
"""