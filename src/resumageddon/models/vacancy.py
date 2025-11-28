from typing import Optional


class Vacancy:
    __slots__ = (
        "title",
        "link",
        "salary",
        "description",
        "requirement",
        "responsibility",
        "salary_str"
    )

    def __init__(
            self,
            title: str,
            link: str,
            salary: int,
            description: str,
            requirement: Optional[str] = "",
            responsibility: Optional[str] = ""
    ):
        self.title = title
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description
        self.requirement = requirement
        self.responsibility = responsibility

    def _validate_salary(self, salary: int) -> int:
        if isinstance(salary, int) and salary >= 0:
            return salary
        return 0


    def __repr__(self) -> str:
        return f"<Vacancy {self.title} ({self.salary})>"

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    def __eq__(self, other):
        return (
            isinstance(other, Vacancy) and
            self.title == other.title and
            self.link == other.link
        )

    def __hash__(self):
        return hash((self.title, self.link))

    @staticmethod
    def _parse_salary(salary_data: dict) -> int:
        if not salary_data:
            return 0
        _from = salary_data.get("from")
        _to = salary_data.get("to")
        if _from and _to:
            return (_from + _to) // 2
        return _from or _to or 0

    @classmethod
    def from_json(cls, data: dict) -> 'Vacancy':
        title = data.get("name", "Без названия")
        link = data.get("alternate_url", "")
        salary_data = data.get("salary")
        salary = cls._parse_salary(salary_data)

        # Строка для отображения
        if not salary_data:
            salary_str = "Зарплата не указана"
        else:
            _from = salary_data.get("from")
            _to = salary_data.get("to")
            currency = salary_data.get("currency", "RUR")

            if _from and _to:
                salary_str = f"{_from:,} – {_to:,} {currency}".replace(",", " ")
            elif _from:
                salary_str = f"от {_from:,} {currency}".replace(",", " ")
            elif _to:
                salary_str = f"до {_to:,} {currency}".replace(",", " ")
            else:
                salary_str = "Зарплата не указана"

        snippet = data.get("snippet", {})
        requirement = snippet.get("requirement", "")
        responsibility = snippet.get("responsibility", "")
        description = f"{requirement} {responsibility}".strip()

        vacancy = cls(
            title=title,
            link=link,
            salary=salary,
            description=description,
            requirement=requirement,
            responsibility=responsibility
        )

        # 👇 Добавляем динамически строку для отображения
        vacancy.salary_str = salary_str
        return vacancy

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description,
            "requirement": self.requirement,
            "responsibility": self.responsibility
        }
