from connector import Connector
class Vacancy:
    __slots__ = ('name', 'link', 'description', 'salary')

    def __init__(self, name, link, description, salary):
        self.name = name
        self.link = link
        self.description = description
        self.salary = salary

    def __eq__(self, other):
        return self.salary == other.salary
    def __lt__(self, other):
        return self.salary < other.salary
    def __le__(self, other):
        return self.salary <= other.salary
    def __gt__(self, other):
        return self.salary > other.salary
    def __ge__(self, other):
        return self.salary >= other.salary

    def __str__(self):
        return f'Название вакансии:{self.name}, ссылка на вакансию:{self.link}, опсание вакансии:{self.description}, З/п вакансии:{self.salary}'



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        connector = Connector()
        connector.data_file = self.json_file
        return len(connector.read_file())



class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    json_file = 'HH_responses.json'
    def __init__(self, name, link, description, salary, company_name):
        super().__init__(name, link, description, salary)
        self.company_name = company_name

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """
    json_file = 'SJ_responses.json'
    def __init__(self, name, link, description, salary, company_name):
        super().__init__(name, link, description, salary)
        self.company_name = company_name

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    return sorted(vacancies, reverse = True)

def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    for i in range(top_count):
        print(vacancies[i])