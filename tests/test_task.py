"""Тесты класса Task"""

from src.models.task import Task
import pytest

def test_create_task_default():
    task = Task()
    assert task.id.startswith("task_")
    assert task.payload is None

def test_create_task_with_payload():
    task = Task(payload={"k": "v"})
    assert task.payload == {"k": "v"}

def test_task_id_unique():
    task1 = Task()
    task2 = Task()
    assert task1.id != task2.id

def test_empty_id():
    with pytest.raises(ValueError, match="не может быть пустым"):
        Task(id="")

def test_tasks_equal_same_id():
    task1 = Task(id="id")
    task2 = Task(id="id")
    assert task1 == task2

def test_tasks_not_equal_different_id():
    task1 = Task(id="id1")
    task2 = Task(id="id2")
    assert task1 != task2

def test_to_dict():
    task = Task(id="test_id", payload={"data": "value"})
    assert task.to_dict() == {"id": "test_id", "payload": {"data": "value"}}

def test_from_dict():
    task = Task.from_dict({"id": "test_id", "payload": "test"})
    assert task.id == "test_id"
    assert task.payload == "test"

def test_from_dict_missing_id():
    with pytest.raises(ValueError, match="должен содержать поле 'id'"):
        Task.from_dict({"payload": "test"})

def test_task_hash():
    task1 = Task(id="hash_test")
    task2 = Task(id="hash_test")
    assert hash(task1) == hash(task2)

def test_task_eq_with_non_task():
    task = Task(id="test_id")
    assert task.__eq__("not_a_task") is NotImplemented
