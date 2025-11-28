from .base_api import VacancyAPI
from .abstract_api import VacancyAPI
import requests
from typing import List, Dict


class HeadHunterAPI(VacancyAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self._headers = {
            "User-Agent": "ResumageddonBot/1.0"
        }

    def _get(self, params: dict):
        """Приватный метод для отправки GET-запроса."""
        response = requests.get(self.BASE_URL, headers=self._headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка при запросе: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword: str):
        """Получает вакансии по ключевому слову с API HH"""
        all_vacancies = []
        params = {
            "text": keyword,
            "per_page": 20,   # можно изменить на 50–100, если хочешь
            "page": 0
        }

        # Можно собрать несколько страниц, если нужно
        for page in range(2):  # пример: 2 страницы
            params["page"] = page
            data = self._get(params)
            items = data.get("items", [])
            if not items:
                break
            all_vacancies.extend(items)

        return all_vacancies
