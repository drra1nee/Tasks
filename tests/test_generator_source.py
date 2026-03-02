"""Тесты генератора задач"""

import pytest
from src.sources.generator_source import GeneratorTaskSource, create_generator_source
from src.contracts.protocol import TaskSource

def test_create_with_custom_count():
    source = GeneratorTaskSource(count=5)
    assert source.count == 5

def test_create_with_negative_count():
    with pytest.raises(ValueError, match="неотрицательным"):
        GeneratorTaskSource(count=-1)

def test_get_tasks_correct_count():
    source = GeneratorTaskSource(count=5)
    tasks = list(source.get_tasks())
    assert len(tasks) == 5

def test_get_tasks_is_valid_source():
    source = GeneratorTaskSource(count=3)
    assert isinstance(source, TaskSource)

def test_payload_str_template():
    source = GeneratorTaskSource(count=3, payload_template="task")
    tasks = list(source.get_tasks())
    assert tasks[0].payload == "task_0"
    assert tasks[1].payload == "task_1"

def test_payload_dict_template():
    source = GeneratorTaskSource(count=2, payload_template={"type": "test"})
    tasks = list(source.get_tasks())
    assert tasks[0].payload == {"type": "test", "index": 0}

def test_payload_list_template():
    source = GeneratorTaskSource(count=2, payload_template=[1, 2])
    tasks = list(source.get_tasks())
    assert tasks[0].payload == [1, 2, 0]
    assert tasks[1].payload == [1, 2, 1]

def test_payload_int_template():
    source = GeneratorTaskSource(count=2, payload_template=42)
    tasks = list(source.get_tasks())
    assert tasks[0].payload == "42_0"
    assert tasks[1].payload == "42_1"

def test_create_generator_source_str():
    source = create_generator_source(count=3, payload_type="string")
    assert isinstance(source, GeneratorTaskSource)
    assert source.payload_template == "task"

def test_create_generator_source_dict():
    source = create_generator_source(count=2, payload_type="dict")
    assert source.payload_template == {"type": "generated"}

def test_create_generator_source_int():
    source = create_generator_source(count=2, payload_type="int")
    assert source.payload_template == 0

def test_create_generator_source_unknown_type():
    source = create_generator_source(count=1, payload_type="unknown")
    assert source.payload_template == "task"
