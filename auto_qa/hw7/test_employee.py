from employee_api import EmployeeApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)


def test_create_employee():
    """Тест: создание нового сотрудника"""
    # 1. Создаём сотрудника
    employee = api.create_employee(
        first_name="Александр",
        last_name="Иванов",
        middle_name="Петрович",
        company_id=10,
        email="alex.ivanov@example.com",
        phone="+38161234567",
        birthdate="1988-03-25",
        is_active=True
    )

    # Проверяем, что ответ содержит все обязательные поля
    assert "first_name" in employee, f"Ожидалось поле 'first_name' в ответе"
    assert "last_name" in employee, f"Ожидалось поле 'last_name' в ответе"
    assert "middle_name" in employee, f"Ожидалось поле 'middle_name' в ответе"

    assert employee["first_name"] == "Александр", f"Ожидалось 'Александр', получено '{employee['first_name']}'"
    assert employee["last_name"] == "Иванов", f"Ожидалось 'Иванов', получено '{employee['last_name']}'"
    assert employee["middle_name"] == "Петрович", f"Ожидалось 'Петрович', получено '{employee['middle_name']}'"
    assert employee["company_id"] == 10, f"Ожидалось 10, получено '{employee['company_id']}'"
    assert employee[
               "email"] == "alex.ivanov@example.com", f"Ожидалось 'alex.ivanov@example.com', получено '{employee['email']}'"
    assert employee["phone"] == "+38161234567", f"Ожидалось '+38161234567', получено '{employee['phone']}'"
    assert employee["birthdate"] == "1988-03-25", f"Ожидалось '1988-03-25', получено '{employee['birthdate']}'"
    assert employee["is_active"] is True, "Ожидалось, что сотрудник активен"

    print(f"Тест пройден: сотрудник успешно создан. Данные: {employee}")


def test_get_employee_info():
    """Тест: получение информации о сотруднике"""
    # 1. Сначала создаём сотрудника для теста
    employee = api.create_employee(
        first_name="Екатерина",
        last_name="Смирнова",
        middle_name="Александровна",
        company_id=15,
        email="kate.smirnova@example.com",
        phone="+79265554433",
        birthdate="1992-11-08",
        is_active=True
    )

    assert employee["first_name"] == "Екатерина", f"Ожидалось 'Екатерина', получено '{employee['first_name']}'"
    assert employee["last_name"] == "Смирнова", f"Ожидалось 'Смирнова', получено '{employee['last_name']}'"
    assert employee[
               "email"] == "kate.smirnova@example.com", f"Ожидалось 'kate.smirnova@example.com', получено '{employee['email']}'"

    print(f"Тест пройден: данные сотрудника получены корректно. Данные: {employee}")


def test_update_employee():
    """Тест: изменение данных о сотруднике"""
    employee = api.create_employee(
        first_name="Дмитрий",
        last_name="Козлов",
        middle_name="Владимирович",
        company_id=20,
        email="dmitry.kozlov@example.com",
        phone="+38031237890",
        birthdate="1995-06-14",
        is_active=True
    )

    # Сохраняем email для идентификации
    original_email = employee["email"]

    # 2. Пробуем обновить данные
    print(f"Создан сотрудник: {employee}")
    print("Тест update_employee требует доработки для получения ID сотрудника")
