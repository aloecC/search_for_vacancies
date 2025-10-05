from src.api_client import HeadHunterAPI
from src.vacancy_service import Vacancy


class UserInteraction:
    """Класс для взаимодействия с пользователем"""
    def __init__(self, search_query, top_n, filter_words, salary_range):
        self.search_query = search_query # поисковой запрос в общем
        self.top_n = top_n
        self.filter_words = filter_words # ключ-слова в requirement
        self.salary_range = salary_range

    @classmethod
    def filter_vacancies(cls, vacancies_list):
        '''Метод фильтрации вакансий по ключ словам'''
        # vacancies_list, filter_words
        filtered_vacancies = []
        for obj in vacancies_list:
            for word in filter_words:
                if word.lower() in obj.requirement.lower():
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
            elif int(obj.salary) in range(int(from_salary), int(to_salary)+1):
                ranged_vacancies.append(obj)
        return ranged_vacancies

    def sort_vacancies(self, ranged_vacancies):
        """Метод сортировки по зарплатам"""
        return ranged_vacancies.sort(key=lambda x: x.salary, reverse=True)

    def get_top_vacancies(self, ranged_vacancies):
        '''Метод вывода топ-N вакансий'''
        return ranged_vacancies[:self.top_n]

platforms = ["HeadHunter"]

#search_query = input("Введите поисковый запрос: ") #Python
#top_n = int(input("Введите количество вакансий для вывода в топ N: ")) #10
#filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split() #SQL Английский HTML CSS JSON
#salary_range = input("Введите диапазон зарплат: ") # Пример: 100000-150000
#user_salary = UserInteraction(search_query, top_n, filter_words, salary_range)


search_query = 'Python'
top_n = 3
filter_words = 'SQL Английский HTML CSS JSON'.split()
salary_range = '100000-520000'.split('-')

user_salary = UserInteraction(search_query, top_n, filter_words, salary_range)
hh_api = HeadHunterAPI()

user_hh_vacancies = hh_api.get_vacancies(search_query, 100) #js файл
user_vacancies_list = Vacancy.get_filtered_vacancies(user_hh_vacancies)

filtered_vacancies = user_salary.filter_vacancies(user_vacancies_list) #obj list

ranged_vacancies = user_salary.get_vacancies_by_salary(filtered_vacancies)

user_salary.sort_vacancies(ranged_vacancies)

#[print(f"{vacancy.name}, Ссылка: {vacancy.url}, ЗП: {vacancy.salary} руб.Требования: {vacancy.requirement}.") for vacancy in ranged_vacancies]
top_vacancies = user_salary.get_top_vacancies(ranged_vacancies)
top_vacancies_str = Vacancy.cast_to_object_list(top_vacancies)
print(f"Ваш топ-{top_n}:")
[print(vacancy) for vacancy in top_vacancies_str]