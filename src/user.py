from src.api.hh_api_client import HeadHunterAPI
from src.models.vacancy_service import Vacancy


class UserInteraction:
    """Класс для взаимодействия с пользователем"""
    def __init__(self, search_query, top_n, filter_words, salary_range):
        self.search_query = search_query  # поисковой запрос в общем
        self.top_n = top_n
        self.filter_words = filter_words.split()  # ключ-слова в requirement
        self.salary_range = salary_range.split('-')

    @classmethod
    def filter_vacancies(cls, vacancies_list):
        '''Метод фильтрации вакансий по ключ словам'''
        # vacancies_list, filter_words
        filtered_vacancies = []
        for obj in vacancies_list:
            for word in filter_words:
                if word.lower() in obj.requirement.lower():
                    if obj not in filtered_vacancies:
                        filtered_vacancies.append(obj)
        return filtered_vacancies

    def get_vacancies_by_salary(self, filtered_vacancies):
        '''Метод сортировки по зарплате'''
        ranged_vacancies = []
        (from_salary, to_salary) = self.salary_range
        for obj in filtered_vacancies:
            if '-' in str(obj.salary):
                (from_obj, to_obj) = obj.salary.split('-')
                if int(from_obj) >= int(from_salary) and int(to_obj) <= int(to_salary):
                    ranged_vacancies.append(obj)
            elif int(obj.salary) in range(int(from_salary), int(to_salary) + 1):
                ranged_vacancies.append(obj)
        return ranged_vacancies

    def sort_vacancies(self, ranged_vacancies):
        """Метод сортировки по зарплатам"""
        return ranged_vacancies.sort(key=lambda x: x.salary, reverse=True)

    def get_top_vacancies(self, ranged_vacancies):
        '''Метод вывода топ-N вакансий'''
        return ranged_vacancies[:self.top_n]


def user_get_top(search_query=None, top_n=None, filter_words=None, salary_range=None):
    '''Функция для взаимодействия с пользователем'''
    platforms = ["HeadHunter"]
    print(f'Здравствуйте! Мы на платформе {platforms}, Давайте подберем вам работу!')

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_range = input("Введите диапазон зарплат: ")

    user_salary = UserInteraction(search_query, top_n, filter_words, salary_range)
    user_hh_api = HeadHunterAPI()

    user_hh_vacancies = user_hh_api.get_vacancies(search_query)  # js файл
    user_vacancies_list = Vacancy.get_filtered_vacancies(user_hh_vacancies)

    filtered_vacancies = user_salary.filter_vacancies(user_vacancies_list)  # obj list

    ranged_vacancies = user_salary.get_vacancies_by_salary(filtered_vacancies)

    user_salary.sort_vacancies(ranged_vacancies)

    top_vacancies = user_salary.get_top_vacancies(ranged_vacancies)

    top_vacancies_str = Vacancy.cast_to_object_list(top_vacancies)

    if len(top_vacancies_str) == 0:
        print('По вашему запросу ничего не найдено, измените критерии поиска и повторите запрос')
        check = input('Нажмите Enter, чтобы продолжить или введите 1 для выхода из поиска: ')
        if check == '':
            user_get_top()
        else:
            return
    else:
        if len(top_vacancies_str) < top_n:
            print("По вашему запросу нашлось меньше вакансий")
            top_n = len(top_vacancies_str)
        print(f"Ваш топ-{top_n}:")
        [print(vacancy) for vacancy in top_vacancies_str]
    return 'Удачного трудоустройства!'


search_query = 'Python'
top_n = 3
filter_words = 'Exel SQL Английский Высшее'
salary_range = '100000-520000'
user_get_top(search_query, top_n, filter_words, salary_range)
