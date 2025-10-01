from src.vacancy_service import Vacancy


class UserWorker:
    def __init__(self):
        pass

    def filter_vacancies(self, vacancies_str, filter_words):
        if 'name' in filter_words and 'url' in filter_words and 'salary' in filter_words and 'requirement' in filter_words:
            return vacancies_str
        else:
            return ('Фильтр-слова не подходят')

    def get_vacancies_by_salary(self, filtered_vacancies, salary_range):
        pass

    def sort_vacancies(self, ranged_vacancies):
        pass

    def get_top_vacancies(self, sorted_vacancies, top_n):
        pass

