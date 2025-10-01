from src.api_client import HeadHunterAPI
from src.file_manager import JSONSaver
from src.utils import UserWorker
from src.vacancy_service import Vacancy
# Создание экземпляра класса для работы с API сайтов с вакансиями
#hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
#hh_vacancies = hh_api.get_vacancies("Python")
#for v in hh_vacancies:
#   print(v)

# Преобразование набора данных из JSON в строчное отображение списка объектов
#vacancies_str = Vacancy.cast_to_object_list(hh_vacancies)
#for f in vacancies_list:
#    print(f)
# Преобразование набора данных из JSON в список объектов
#vacancies_list = Vacancy.get_filtered_vacancies(hh_vacancies)
# Пример работы контструктора класса с одной вакансией
#vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000", "Требования: опыт работы от 3 лет...")
# Сохранение информации о вакансиях в файл
#json_saver = JSONSaver()
#json_saver.adding_data_to_file(vacancy)
#json_saver.adding_data_to_file(vacancies_list)
#json_saver.deleting_data_from_a_file(vacancy)

# Функция для взаимодействия с пользователем

platforms = ["HeadHunter"]
search_query = input("Введите поисковый запрос: ")
top_n = int(input("Введите количество вакансий для вывода в топ N: "))
filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
salary_range = input("Введите диапазон зарплат: ") # Пример: 100000-150000

hh_api = HeadHunterAPI()
user = UserWorker()

hh_vacancies = hh_api.get_vacancies(search_query, top_n)

vacancies_str = Vacancy.cast_to_object_list(hh_vacancies)

filtered_vacancies = user.filter_vacancies(vacancies_str, filter_words)
print(filtered_vacancies)
#    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

 #   sorted_vacancies = sort_vacancies(ranged_vacancies)
  #  top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
   # print_vacancies(top_vacancies)