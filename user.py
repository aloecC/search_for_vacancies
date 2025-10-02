# Функция для взаимодействия с пользователем

from src.api_client import HeadHunterAPI
from src.vacancy_service import Vacancy


class UserInteraction:
    def __init__(self, search_query, top_n, filter_words, salary_range):
        self.search_query = search_query # поисковой запрос в общем
        self.top_n = top_n
        self.filter_words = filter_words # ключ-слова в requirement
        self.salary_range = [salary_range.slit('-')]# диапазон зарплаты min и max

    @classmethod
    def filter_vacancies(cls, vacancies_list):
        '''Метод фильтрации вакансий по ключ словам'''
        # vacancies_list, filter_words
        filtered_vacancies = []
        for obj in vacancies_list:
            for word in filter_words:
                if word.lower() in (obj['requirement']).lower():
                    filtered_vacancies.append(obj)
        return filtered_vacancies

    def sort_vacancies(self):
        '''Метод'''
        # ranged_vacancies
        pass

    def get_top_vacancies(self):
        '''Метод'''
        # sorted_vacancies, top_n
        pass




platforms = ["HeadHunter"]
search_query = input("Введите поисковый запрос: ")
top_n = int(input("Введите количество вакансий для вывода в топ N: "))
filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
salary_range = input("Введите диапазон зарплат: ") # Пример: 100000-150000
user_vacancy = UserInteraction(search_query, top_n, filter_words, salary_range)

hh_api = HeadHunterAPI()
user = UserInteraction()

hh_vacancies = hh_api.get_vacancies(search_query) # js файл
vacancies_list = Vacancy.get_filtered_vacancies(hh_vacancies)
filtered_vacancies = user.filter_vacancies() #obj list

#ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

#sorted_vacancies = sort_vacancies(ranged_vacancies)

#top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

#print_vacancies(top_vacancies)