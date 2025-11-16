from .base_api import VacancyAPI
import requests
from typing import List, Dict

class HeadHunterAPI(VacancyAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str) -> List[Dict]:
        # Это мы потом напишем
        return []
