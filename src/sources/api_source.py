"""Модуль API-заглушки"""

from typing import Iterator
from ..models.task import Task

class APITaskSource:
    """API-заглушка для имитации внешнего источника задач"""

    def __init__(self, tasks_data: list[dict] | None = None) -> None:
        """Инициализирует API-заглушку"""
        self._tasks_data = tasks_data or self._get_default_tasks()

    def _get_default_tasks(self) -> list[dict]:
        """Возвращает данные задач по умолчанию"""
        return [
            {"id": "api_task_1", "payload": {"action": "notify", "user_id": 1}},
            {"id": "api_task_2", "payload": {"action": "process", "order_id": 67}},
            {"id": "api_task_3", "payload": {"action": "check", "resource": "db"}},
        ]

    def get_tasks(self) -> Iterator[Task]:
        """Генерирует итератор задач из API-заглушки"""
        for task_data in self._tasks_data:
            yield Task(id=task_data["id"], payload=task_data.get("payload"))

    def refresh(self) -> None:
        """Имитирует обновление данных из API"""
        self._tasks_data = self._get_default_tasks()

def create_api_source(tasks_count: int = 3) -> APITaskSource:
    """Функция для создания API-заглушки"""
    tasks_data = [
        {"id": f"api_task_{i + 1}", "payload": {"action": "job", "index": i}}
        for i in range(tasks_count)
    ]
    return APITaskSource(tasks_data=tasks_data)
