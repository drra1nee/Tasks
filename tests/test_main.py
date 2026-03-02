"""Тесты для main"""

from src.main import main

def test_main_runs_without_error(capsys):
    main()
    captured = capsys.readouterr()
    assert "Платформа обработки задач" in captured.out

def test_main_prints_contract_check(capsys):
    main()
    captured = capsys.readouterr()
    assert "Контракт соблюдён:" in captured.out

def test_main_prints_tasks(capsys):
    main()
    captured = capsys.readouterr()
    assert "Задачи:" in captured.out
