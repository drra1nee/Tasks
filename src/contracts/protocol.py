"""Контракты для источников задач"""

from typing import Protocol, Iterator, runtime_checkable
from src.models.task import Task

@runtime_checkable
class TaskSource(Protocol):
    """
    Контракт для всех источников задач
    Любой источник должен реализовать метод get_tasks()
    """
    def get_tasks(self) -> Iterator[Task]:
        """Вернуть итератор с задачами"""
        ...

def validate_source(source: object) -> TaskSource:
    """Проверить что источник соблюдает контракт"""
    if not isinstance(source, TaskSource):
        raise TypeError(
            f"Объект {type(source).__name__} не реализует TaskSource"
            f"Добавьте метод get_tasks() -> Iterator[Task]"
        )
    return source


def is_valid_source(source: object) -> bool:
    """Проверить что источник соблюдает контракт (без ошибки)"""
    return isinstance(source, TaskSource)
