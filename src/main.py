"""Демонстрация платформы обработки задач"""
from src.contracts.protocol import validate_source
from src.sources.generator_source import create_generator_source
from src.sources.api_source import create_api_source

def demo_generator_source() -> None:
    """Демонстрация источника-генератора"""
    print("Источник: Генератор задач:")
    source = create_generator_source(count=3, payload_type="dict")
    if validate_source(source):
        print("Контракт соблюден: GeneratorTaskSource")
    for task in source.get_tasks():
        print(f"  {task.id}: {task.payload}")

def demo_api_source() -> None:
    """Демонстрация API-заглушки"""
    print("Источник: API-заглушка:")
    source = create_api_source(tasks_count=3)
    if validate_source(source):
        print("Контракт соблюден: APITaskSource")
    for task in source.get_tasks():
        print(f"  {task.id}: {task.payload}")


def main() -> None:
    """Точка входа платформы"""
    print("ПЛАТФОРМА ОБРАБОТКИ ЗАДАЧ")
    demo_generator_source()
    demo_api_source()

if __name__ == "__main__":
    main()
