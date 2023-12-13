import doctest

class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param make: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)  # инициализация экземпляра класса
        """
        if not isinstance(make, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска автомобиля должен быть целым числом")
        if year <= 0:
            raise ValueError("Год выпуска автомобиля должен быть положительным числом")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запустить двигатель автомобиля.

        :return: Сообщение о запуске двигателя

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.start_engine()
        """
        ...

    def accelerate(self, speed: int) -> str:
        """
        Ускорить автомобиль до указанной скорости.

        :param speed: Желаемая скорость
        :return: Сообщение об ускорении

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.accelerate(60)
        """
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть целым числом")
        if speed < 0:
            raise ValueError("Скорость должна быть неотрицательным числом")
        ...

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")

        self.title = title
        self.author = author
        self.pages = pages

    def is_long_book(self, max_pages: int = 500) -> bool:
        """
        Функция, которая проверяет, является ли книга длинной (более 500 страниц).

        :param max_pages: Максимальное количество страниц для определения длинной книги
        :return: Является ли книга длинной

        Примеры:
        >>> book = Book("1984", "George Orwell", 600)
        >>> book.is_long_book()
        """
        ...
    def recommend(self, reader_age: int) -> str:
        """
        Рекомендовать книгу пределенному возрасту читателей.

        :param reader_age: Возраст читателя
        :return: Рекомендация

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.recommend(16)
        """
        if not isinstance(reader_age, int):
            raise TypeError("Возраст читателя должен быть целым числом")
        if reader_age < 0:
            raise ValueError("Возраст читателя должен быть неотрицательным числом")
        ...

class Movie:
    def __init__(self, title: str, director: str, duration_minutes: int):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param title: Название фильма
        :param director: Режиссер фильма
        :param duration_minutes: Продолжительность фильма в минутах

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название фильма должно быть строкой")
        if not isinstance(director, str):
            raise TypeError("Режиссер фильма должен быть строкой")
        if not isinstance(duration_minutes, int):
            raise TypeError("Продолжительность фильма должна быть целым числом")
        if duration_minutes <= 0:
            raise ValueError("Продолжительность фильма должна быть положительным числом")

        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes

    def pause_movie(self) -> str:
        """
        Поставить фильм на паузу.

        :return: Сообщение о постановке на паузу

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)
        >>> movie.pause_movie()
        """
        ...

    def add_subtitles(self, language: str) -> str:
        """
        Добавить субтитры на выбранном языке.

        :param language: Язык для субтитров
        :return: Сообщение о добавлении субтитров

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)
        >>> movie.add_subtitles("Russian")
        """
        if not isinstance(language, str):
            raise TypeError("Язык для субтитров должен быть строкой")
        ...
if __name__ == "__main__":
    doctest.testmod()