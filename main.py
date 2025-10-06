from src.api.hh_api_client import HeadHunterAPI
from src.handler_file.json_handler import JSONSaver
from src.models.vacancy_service import Vacancy

#Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python", 50)
# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.get_filtered_vacancies(hh_vacancies)
# Преобразование набора данных из JSON в строчное отображение списка объектов
#vacancies_str = Vacancy.cast_to_object_list(vacancies_list)
# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000", "Опыт работы от 3 лет...")
# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.adding_data_to_file(vacancy)
json_saver.adding_data_to_file(vacancies_list)
#json_saver.deleting_data_from_a_file(vacancy)