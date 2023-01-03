
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
        if self.salary:
            return f'Название вакансии:{self.name}, ссылка на вакансию:{self.link}, описание вакансии:{self.description}, З/п вакансии:{self.salary}'
        else:
            return f'Название вакансии:{self.name}, ссылка на вакансию:{self.link}, описание вакансии:{self.description}, З/п не указана'

    def __repr__(self):
        if self.salary:
            return f'Название вакансии:{self.name}, ссылка на вакансию:{self.link}, описание вакансии:{self.description}, З/п вакансии:{self.salary}'
        else:
            return f'Название вакансии:{self.name}, ссылка на вакансию:{self.link}, описание вакансии:{self.description}, З/п не указана'
class CountMixin:
    counter = 0

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        return CountMixin.counter

    @get_count_of_vacancy.setter
    def get_count_of_vacancy(self, value):
        CountMixin.counter = value


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    json_file = 'HH_responses.json'
    data = []
    def __init__(self, name, link, description, salary, company_name):
        self.get_count_of_vacancy += 1
        super().__init__(name, link, description, salary)
        self.company_name = company_name

    def __str__(self):
        return f'Вакансия с сайта HeadHunter: Название компании: {self.company_name}, ' + super().__str__()

    def __repr__(self):
        return f'Вакансия с сайта HeadHunter: Название компании: {self.company_name}, ' + super().__repr__()


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """
    json_file = 'SJ_responses.json'
    data = []
    def __init__(self, name, link, description, salary, company_name):
        self.get_count_of_vacancy += 1
        super().__init__(name, link, description, salary)
        self.company_name = company_name

    def __str__(self):
            return f'Вакансия с сайта SuperJob: {self.company_name}, ' + super().__str__()


    def __repr__(self):
            return f'Вакансия с сайта SuperJob: {self.company_name}, ' + super().__repr__()



def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    return sorted(vacancies, reverse = True)

def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    for i in range(top_count):
        print(f'Вакансия номер {i + 1}', vacancies[i])