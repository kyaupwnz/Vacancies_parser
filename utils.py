from jobs_classes import *
import json


def init_HH():
    with open('data/HH_responses.json', 'r', encoding='utf-8') as file:
        reader = json.load(file)
        for vacancy in reader[0]:
            name = vacancy.get('name')
            link = vacancy.get('alternate_url')
            try:
                description =  vacancy['snippet'].get('requirement') + ' ' + vacancy['snippet'].get('responsibility')
            except:
                description = None
            try:
                if vacancy['salary'].get('from'):
                    salary = vacancy['salary'].get('from')
                elif vacancy['salary'].get('to'):
                    salary = vacancy['salary'].get('to')
            except:
                salary = 0
            company_name = vacancy['employer'].get('name')
            HHVacancy.data.append(HHVacancy(name, link, description, salary, company_name))
        return HHVacancy.data


def init_SJ():
    with open('data/SJ_responses.json', 'r', encoding='utf-8') as file:
        reader = json.load(file)
        for vacancy in reader[0]:
            name = vacancy.get('profession')
            link = vacancy.get('link')
            description = vacancy.get('candidat')
            try:
                if vacancy.get('payment_from'):
                    salary = vacancy.get('payment_from')
                elif vacancy.get('payment_to'):
                    salary = vacancy.get('payment_to')
            except:
                salary = 0
            company_name = vacancy.get('firm_name')
            SJVacancy.data.append(SJVacancy(name, link, description, salary, company_name))
        return SJVacancy.data


