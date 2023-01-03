from engine_classes import *
from jobs_classes import *
from utils import *
if __name__ == '__main__':
    input_word = input('Введите поисковый запрос:')
    vacancies_count = input('Введите количество вакансий в поисковом запросе:')
    top_count = int(input('Введите количество вакансий для вывода в терминал:'))
    hh = HH(input_word, vacancies_count)
    hh.get_request(input_word, vacancies_count)
    sj = SuperJob(input_word, vacancies_count)
    sj.get_request(input_word, vacancies_count)
    data_hh = init_HH()
    data_sj = init_SJ()
    data_hh_sorted = sorting(data_hh)
    data_sj_sorted = sorting(data_sj)
    get_top(data_hh_sorted, top_count)
    get_top(data_sj_sorted, top_count)

