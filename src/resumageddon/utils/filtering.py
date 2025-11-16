def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    return [v for v in vacancies if keyword.lower() in v.description.lower()]

def sort_by_salary(vacancies: List[Vacancy], reverse=True):
    return sorted(vacancies, reverse=reverse)

def get_top_n(vacancies: List[Vacancy], n: int):
    return vacancies[:n]
