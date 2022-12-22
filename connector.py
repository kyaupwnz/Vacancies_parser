import json
import os
cwd = os.getcwd()
class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = os.path.join(cwd, value)
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        data = []
        try:
            with open(self.__data_file, 'r', encoding = 'utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(self.__data_file, 'w', encoding = 'utf-8') as file:
                json.dump(data, file)
        finally:
            file.close()
        return data

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__data_file, 'r', encoding = 'utf-8') as file:
            new_data = json.load(file)
            new_data.append(data)
            file.close()
        with open(self.__data_file, 'w', encoding = 'utf-8') as file:
            json.dump(new_data, file)
            file.close()
    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(self.__data_file, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
            file.close()
        if not len(query):
            return data
        query_data = []
        for key in data[query.keys()]:
            if data[key] == query.values():
                query_data.append(data[key])
        return query_data

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        if not len(query):
            return
        with open(self.__data_file, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
            file.close()
        counter = 0
        for key in data:
            if key.get(list(query.keys())[0]) == list(query.values())[0]:
                del data[counter]
            counter += 1
        with open(self.__data_file, 'w', encoding = 'utf-8') as file:
            json.dump(data, file)
            file.close()



if __name__ == '__main__':
    df = Connector()
    df.data_file = 'df.json'

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id':1})
    data_from_file = df.select(dict())
    assert data_from_file == []