from src.api_client import HeadHunterAPI
from src.vacancy_service import Vacancy
# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")
for v in hh_vacancies:
    print(v)

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
for f in vacancies_list:
    print(f)

# Пример работы контструктора класса с одной вакансией
#vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
#json_saver = JSONSaver()
#json_saver.add_vacancy(vacancy)
#json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
