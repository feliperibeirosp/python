class DataTable:
    def __init__(self, name, data=[]):
        self._name = name
        self._data = data

    def add_row(self, row):
        self._data.append(row)

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return self.name == other.name


t1 = DataTable("ExecucaoFinanceira1")
t2 = DataTable("ExecucaoFinanceira")


print(t1 == t2)
print(t2.__dict__)