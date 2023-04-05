from datetime import datetime


def function_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.utcnow()
        try:
            func(*args, **kwargs)
            stop_time = datetime.utcnow()
            print(f'Время выполнение функции: {stop_time - start_time} ')

            return func(*args, **kwargs)

        except Exception as e:
            print(f"Ошибка: {e.__class__}, в функции: {func.__name__}")

    return wrapper