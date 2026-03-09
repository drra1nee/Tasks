"""Тесты API-заглушки источника задач"""
from src.sources.api_source import APITaskSource, create_api_source
from src.contracts.protocol import TaskSource, validate_source

def test_create_api_source_default():
    source = APITaskSource()
    tasks = list(source.get_tasks())
    assert len(tasks) == 3
    assert tasks[0].id == "task_1"

def test_create_api_source_custom_data():
    custom_data = [{"action": "404"}, {"action": "67"},]
    source = APITaskSource(tasks_data=custom_data)
    tasks = list(source.get_tasks())
    assert len(tasks) == 2
    assert tasks[0].payload == {"action": "404"}

def test_api_source_implements_contract():
    source = APITaskSource()
    assert isinstance(source, TaskSource)
    assert validate_source(source) is True

def test_create_api_source():
    source = create_api_source(tasks_count=5)
    tasks = list(source.get_tasks())
    assert len(tasks) == 5

def test_api_source_refresh():
    custom_data = [{"payload": "temp"}]
    source = APITaskSource(tasks_data=custom_data)
    assert len(list(source.get_tasks())) == 1
    source.refresh()
    assert len(list(source.get_tasks())) == 3
