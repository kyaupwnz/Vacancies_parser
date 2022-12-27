from abc import ABC, abstractmethod
from connector import Connector
import requests

class Engine(ABC):
    def __init__(self, input_word, page=10, per_page=10, vacancies_count=100):
        self.input_word = input_word
        self.page = page
        self.per_page = per_page
        self.vacancies_count = vacancies_count
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connector = Connector()
        connector.data_file = file_name
        return connector


class HH(Engine):
    def get_request(self):
        result = []
        page = 0
        while self.per_page * page <= self.vacancies_count:
            response = requests.get(f'https://api.hh.ru/vacancies?page={page}&per_page={self.per_page}&text={self.input_word}')
            if response.status_code == 200:
                result.extend(response.json().get('items'))
                page += 1
        print(len(result))
        json_file = HH.get_connector('data/HH_responses.json')
        json_file.insert(result)
class SuperJob(Engine):
    def get_request(self, input_word):
        pass


if __name__ == '__main__':
    hh = HH('python Томск Senior Django')
    #sj = Superjob()
