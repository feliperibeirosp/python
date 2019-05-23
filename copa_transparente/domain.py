
import unittest
from decimalexemplo import Decimal


class DataTable:
    """Representa uma Tabela de dados.

    Essa classe representa uma tabela de dados do portal
    da transparência. Deve ser capaz de validar linhas
    inseridas de acordo com as colunas que possui. As
    linhas inseridas ficam registradas dentro dela.

    Attributes:
        name: Nome da tabela
        columns: [Lista de colunas]
        data: [Lista de dados]
    
    """
    def __init__(self, name):
        """Construtor

            Args:
                name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self._data = []
        self._references = []
        self._referenced = []

    def _get_name(self):
        print("Getter executado!")
        return self._name

    def _set_name(self, name):
        print("Setter executado!")
        self._name = name

    def _del_name(self):
        print("Deletter executado!")
        raise AttributeError("Não pode deletar esse atributo")

    name = property(_get_name, _set_name, _del_name)
    references = property(lambda self: self._references)
    referenced = property(lambda self: self._referenced)

    def add_column(self, name, kind, description=""):
        self._validate_kind(kind)
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")

    def add_references(self, name, to, on):
        """Cria uma referencia dessa tabela para uma outra tabela

        Args:
            name: nome da relação
            to: instância da tabela apontada
            on: instância coluna em que existe a relação
        """

        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referencia para outra tabela que aponta para
        essa.

        Args:
            name: nome da relação
            by: instância da tabela que aponta para essa
            on: instância coluna em que existe a relação
        """

        relationship = Relationship(name, self, by, on)
        self._referenced.append(relationship)


class Column:
    """Representa uma coluna em um DataTable
    Essa classe contém as informações de uma coluna
    e deve validar um dado de acordo com o tipo de
    dado configurado no construtor.

    Attributes:
        name: Nome da Coluna
        kind: Tipo do Dado (varchar, bigint, numeric)
        description: Descrição da coluna
    """
    def __init__(self, name, kind, description=""):
        """Construtor

            Args:
                name: Nome da Coluna
                kind: Tipo do Dado (varchar, bigint, numeric)
                description: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)

        if self._is_pk:
            _str = "({}) {}".format("PK", _str)

        return _str

    @staticmethod
    def validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True


class ColumnTest(unittest.TestCase):

    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue(not Column.validate('bigint', 10.1))
        self.assertTrue(not Column.validate('bigint', 'texto'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue(not Column.validate('numeric', 'texto'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'texto'))
        self.assertTrue(not Column.validate('varchar', 100))
        self.assertTrue(not Column.validate('varchar', 10.1))


if __name__ == "__main__":
    unittest.main()


class Relationship:
    """Classe que representa um relacionamento entre DataTables

       Essa classe tem todas as informações que identificam um
       relacionamento entre tabelas. Em qual coluna ele existe,
       de onde vem e pra onde vai.
    """

    def __init__(self, name, _from, to, on):
        """Construtor

           Args:
               name: Nome
               from: Tabela de onde sai
               to: Tabela pra onde vai
               on: instância de coluna onde existe
        """
       
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col : {} : {} {}".format(self._name, self._kind, self._description)

        return "{} - {}".format('PK', _str)