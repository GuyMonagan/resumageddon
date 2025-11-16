import json
import os
from typing import List
from .base_storage import VacancyStorage
from ..models.vacancy import Vacancy

class JSONSaver(VacancyStorage):
    def __init__(self, filename: str = "data/vacancies.json"):
        self._filename = filename
        if not os.path.exists(self._filename):
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass  # заглушка

    def get_vacancies(self) -> List[Vacancy]:
        pass  # заглушка

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass  # заглушка
