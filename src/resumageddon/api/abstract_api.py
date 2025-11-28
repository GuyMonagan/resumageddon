from abc import ABC, abstractmethod
from typing import List, Dict

class VacancyAPI(ABC):
    @abstractmethod
    def _get(self, params: dict) -> dict:
        """Приватный метод подключения к API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получить список вакансий по ключевому слову."""
        pass