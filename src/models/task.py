"""Модель задачи"""

from dataclasses import dataclass, field
from typing import Any

_task_counter = 0

def _generate_id():
    """Генерирует уникальный код задачи"""
    global _task_counter
    _task_counter += 1
    return f"task_{_task_counter}"

@dataclass
class Task:
    """Задача платформы обработки"""
    id: str = field(default_factory=_generate_id)
    payload: Any = None

    def __post_init__(self):
        """Проверка после создания задачи"""
        if not self.id:
            raise ValueError("Идентификатор задачи не может быть пустым")

    def __eq__(self, other):
        """Сравнение задач по идентификатору"""
        if not isinstance(other, Task):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        """Хеш на основе идентификатора"""
        return hash(self.id)

    def to_dict(self) -> dict:
        """Превращает задачу в словарь"""
        return {"id": self.id, "payload": self.payload}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Создает задачу из словаря"""
        if "id" not in data:
            raise ValueError("Словарь должен содержать поле 'id'")
        return cls(id=data["id"], payload=data.get("payload"))
