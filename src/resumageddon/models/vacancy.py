from typing import Optional

class Vacancy:
    __slots__ = ("title", "link", "salary", "description")

    def __init__(self, title: str, link: str, salary: Optional[int], description: str) -> None:
        self.title = title
        self.link = link
        self.salary = salary if salary is not None else 0
        self.description = description

    def __repr__(self) -> str:
        return f"<Vacancy {self.title} ({self.salary})>"

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    def __eq__(self, other: "Vacancy") -> bool:
        return self.salary == other.salary


    @classmethod
    def from_json(cls, data: dict) -> "Vacancy":
        title = data.get("name", "Нет названия")
        link = data.get("alternate_url", "Нет ссылки")

        # Разбираем зарплату (может быть None)
        salary_info = data.get("salary")
        if salary_info and salary_info.get("from"):
            salary = salary_info["from"]
        else:
            salary = 0

        snippet = data.get("snippet", {})
        description = snippet.get("requirement") or snippet.get("responsibility") or "Нет описания"

        return cls(title, link, salary, description)
