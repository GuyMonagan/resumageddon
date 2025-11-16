from typing import Optional


class Vacancy:
    __slots__ = (
        "title",
        "link",
        "salary",
        "description",
        "requirement",
        "responsibility"
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
        self.salary = salary
        self.description = description
        self.requirement = requirement
        self.responsibility = responsibility

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
        salary = cls._parse_salary(data.get("salary"))

        snippet = data.get("snippet", {})
        requirement = snippet.get("requirement", "")
        responsibility = snippet.get("responsibility", "")
        description = f"{requirement} {responsibility}".strip()

        return cls(
            title=title,
            link=link,
            salary=salary,
            description=description,
            requirement=requirement,
            responsibility=responsibility
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description,
            "requirement": self.requirement,
            "responsibility": self.responsibility
        }
