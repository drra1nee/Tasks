"""Модуль генератора задач"""

from typing import Iterator, Any
from ..models.task import Task


class GeneratorTaskSource:
    """Генератор задач для тестирования и демонстрации"""

    def __init__(self, count: int = 10, payload_template: Any = "default_payload") -> None:
        """Инициализировать генератор задач
        count: количество задач для генерации
        payload_template: шаблон для payload
        """
        if count < 0:
            raise ValueError(f"count должен быть неотрицательным: {count}")
        self.count = count
        self.payload_template = payload_template

    def get_tasks(self) -> Iterator[Task]:
        """Сгенерировать итератор задач"""
        for i in range(1, self.count):
            payload = self._generate_payload(i)
            yield Task(payload=payload)

    def _generate_payload(self, index: int) -> Any:
        """Сгенерировать payload с индексом"""
        if isinstance(self.payload_template, str):
            return f"{self.payload_template}_{index}"
        elif isinstance(self.payload_template, dict):
            return {**self.payload_template, "index": index}
        elif isinstance(self.payload_template, list):
            return self.payload_template + [index]
        else:
            return f"{self.payload_template}_{index}"



def create_generator_source(count: int = 10,payload_type: str = "string") -> GeneratorTaskSource:
    """Функция для создания генератора"""
    templates = {
        "string": "task",
        "dict": {"type": "generated"},
        "int": 0,
    }
    return GeneratorTaskSource(count=count, payload_template=templates.get(payload_type, "task"))
