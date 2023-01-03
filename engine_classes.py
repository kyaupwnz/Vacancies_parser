from abc import ABC, abstractmethod
from connector import Connector
import requests

class Engine(ABC):
    def __init__(self, input_word, page=0, per_page=20, vacancies_count=100):
        self.input_word = input_word
        self.page = page
        self.per_page = per_page
        self.vacancies_count = vacancies_count
    @abstractmethod
    def get_request(self, input_word, vacancies_count):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connector = Connector()
        connector.data_file = file_name
        return connector


class HH(Engine):
    def get_vacancies(self, input_word, page):
        response = requests.get(f'https://api.hh.ru/vacancies?page={page}&text={input_word}')
        if response.status_code == 200:
            return response.json()
        return None
    def get_request(self, input_word, vacancies_count):
        page = 0
        result = []
        vacancies_found = self.get_vacancies(input_word, page).get('found')
        if self.vacancies_count > vacancies_found:
            self.vacancies_count = vacancies_found
        while self.per_page * page < self.vacancies_count:
            tmp_result = self.get_vacancies(input_word, page)
            if tmp_result:
                result += tmp_result.get('items')
                page += 1
            else:
                break
        json_file = HH.get_connector('data/HH_responses.json')
        json_file.insert(result)



class SuperJob(Engine):
    very_secret_key = 'v3.r.137233612.708c594d2236b787f2054970ef2f9ccb6a23f5a0.689d69c89b3e3e5864670c58565486c6319767d7'
    def get_vacancies(self, input_word, page):
        headers = {'X-Api-App-Id': self.very_secret_key,
                   'Authorization': 'Bearer r.000000010000001.example.access_token',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.get(f'https://api.superjob.ru/2.0/vacancies?page={page}&keyword={input_word}', headers = headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_request(self, input_word, vacancies_count):
        page = 0
        result = []
        vacancies_found = self.get_vacancies(input_word, page).get('total')
        if self.vacancies_count > vacancies_found:
            self.vacancies_count = vacancies_found
        while self.per_page * page < self.vacancies_count:
            tmp_result = self.get_vacancies(input_word, page)
            if tmp_result:
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        json_file = SuperJob.get_connector('data/SJ_responses.json')
        json_file.insert(result)


if __name__ == '__main__':
    #hh = HH('python Томск Senior Django')
    #hh.get_request('python Томск ', 100)
    sj = SuperJob('python')
    sj.get_request('python', 100)

