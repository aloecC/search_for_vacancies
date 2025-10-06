import unittest

from src.models.vacancy_service import Vacancy


class TestVacancyValidation(unittest.TestCase):
    def setUp(self):
        self.vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000", "Требования: опыт работы от 3 лет...")

    def test_valid_name(self):

        # Тестируем корректное название
        self.assertEqual(self.vacancy._validate_name("Вакансия"), "Вакансия")
        self.assertEqual(self.vacancy._validate_name("  Вакансия  "), "Вакансия")

    def test_valid_url(self):
        self.assertEqual(self.vacancy._validate_url("<https://hh.ru/vacancy/123456>"), '<https://hh.ru/vacancy/123456>')

    def test_empty_string(self):
        # Тестируем пустую строку
        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_name("")
        self.assertEqual(str(context.exception), "Название вакансии должно быть непустой строкой.")

        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_url("")
        self.assertEqual(str(context.exception), "URL вакансии должно быть непустой строкой.")

    def test_non_string_input(self):
        # Тестируем некорректные типы
        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_name(123)
        self.assertEqual(str(context.exception), "Название вакансии должно быть непустой строкой.")

        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_name(None)
        self.assertEqual(str(context.exception), "Название вакансии должно быть непустой строкой.")

        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_url(123)
        self.assertEqual(str(context.exception), "URL вакансии должно быть непустой строкой.")

        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_url(None)
        self.assertEqual(str(context.exception), "URL вакансии должно быть непустой строкой.")

    def test_whitespace_string(self):
        # Тестируем строку, состоящую только из пробелов
        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_name("   ")
        self.assertEqual(str(context.exception), "Название вакансии должно быть непустой строкой.")

        with self.assertRaises(ValueError) as context:
            self.vacancy._validate_url("   ")
        self.assertEqual(str(context.exception), "URL вакансии должно быть непустой строкой.")


class TestVacancyComparison(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000", "Требования: опыт работы от 3 лет...")
        self.vacancy2 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "120000-250000", "Требования: опыт работы от 3 лет...")
        self.vacancy3 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "250000", "Требования: опыт работы от 3 лет...")
        self.vacancy4 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "450000", "Требования: опыт работы от 3 лет...")

    def test_eq(self):
        self.assertFalse(self.vacancy1 == self.vacancy2)

    def test_lt(self):
        self.assertTrue(self.vacancy3 < self.vacancy4)

    def test_le(self):
        self.assertTrue(self.vacancy3 <= self.vacancy4)

    def test_gt(self):
        self.assertTrue(self.vacancy4 > self.vacancy3)

    def test_ge(self):
        self.assertTrue(self.vacancy4 >= self.vacancy3)


if __name__ == '__main__':
    unittest.main()
