from src.resumageddon.utils.debug_loader import load_vacancies_from_file
from src.resumageddon.utils.filtering import filter_by_keyword, sort_by_salary, get_top_n
from typing import List
from ..models.vacancy import Vacancy

def print_vacancies(vacancies):
    for v in vacancies:
        print(f"{v.title} | {v.salary} руб. | {v.link}")
        print(f"Описание: {v.description}")
        print("-" * 60)

def main():
    print("🧠 Resumageddon запущен. Жди боль.")

    vacancies = load_vacancies_from_file("data/hh_dump.json")
    print(f"Загружено {len(vacancies)} вакансий из локального файла.")

    keyword = input("Введите ключевое слово для фильтрации (например 'Django'): ")
    filtered = filter_by_keyword(vacancies, keyword)

    sorted_vacancies = sort_by_salary(filtered)
    top_n = int(input("Сколько топовых вакансий вывести? "))
    top_vacancies = get_top_n(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)

if __name__ == "__main__":
    main()
