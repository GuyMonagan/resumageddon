from typing import List
from src.resumageddon.models.vacancy import Vacancy


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    keyword = keyword.lower()
    return [
        v for v in vacancies
        if keyword in v.description.lower()
        or keyword in v.title.lower()
    ]

def sort_by_salary(vacancies: List[Vacancy], reverse=True):
    return sorted(vacancies, reverse=reverse)

def get_top_n(vacancies: List[Vacancy], n: int):
    return vacancies[:n]
