class Proxy:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        print("Acesso ao atributo {}".format(item))
        if hasattr(self.obj, item):
            return getattr(self.obj, item)
        else:
            raise Exception("Atributo desconhecido")


class DataTable:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        print("Atributo não definido '{}' acessado".format(item))

        if item == "data":
            return []
        raise AttributeError("Atributo '{}' não existe".format(item))

    def __getattribute__(self, item):
        print("Attributo {} acessado".format(item))
        return object.__getattribute__(self, item)

# def __setattr__(self, key, value):
#         raise Exception("Classe de leitura apenas")


class Query:
    def __init__(self, attributes):
        self.attributes = attributes
#
#
# table_proxy = Proxy(DataTable('ExecucaoFinanceira'))
# query_proxy = Proxy(Query(['id', 'valor']))
# print(table_proxy.__dict__)
# print(query_proxy.__dict__)
# print(table_proxy.name)
# print(query_proxy.attributes)

# table = DataTable()
# table.name = "ExecucaoFinanceira"

t = DataTable("ExecucaoFinanceira")
print(t._name)
print(t.data)
print(t.cols)
