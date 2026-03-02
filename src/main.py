"""Демонстрация платформы обработки задач"""

from .contracts.protocol import validate_source
from .sources.generator_source import GeneratorTaskSource, create_generator_source

def main() -> None:
    print("Платформа обработки задач\n")

    # Создание источника
    source = GeneratorTaskSource(count=5, payload_template="task")

    # Проверка контракта
    print(f"Контракт соблюдён: {validate_source(source)}")

    # Получение и вывод задач
    print("\nЗадачи:")
    for task in source.get_tasks():
        print(f"  {task.id}: {task.payload}")

    # Фабрика
    print("\ndict payload:")
    factory_source = create_generator_source(count=3, payload_type="dict")
    for task in factory_source.get_tasks():
        print(f"  {task.id}: {task.payload}")


if __name__ == "__main__":
    main()
