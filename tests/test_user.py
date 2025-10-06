import unittest

from src.api.hh_api_client import HeadHunterAPI
from src.user import UserInteraction, search_query, filter_words, salary_range


class TestUserInteraction(unittest.TestCase):
    def setUp(self):
        self.user_salary = UserInteraction('Python', 3, filter_words, salary_range)
        self.user_hh_api = HeadHunterAPI()
        self.user_hh_vacancies = self.user_hh_api.get_vacancies(search_query, 100)

    def test_filter_vacancies(self):
        pass


if __name__ == '__main__':
    unittest.main()
