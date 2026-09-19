from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2      тут походу ошибка в заготовке, выдает AtrributeError. Я поправил самостоятельно.
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_genre_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('11/22/63')
        assert collector.get_book_genre('11/22/63') == ''

    @pytest.mark.parametrize('name', [
    '',
    'a' * 41
])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0


    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('11/22/63')
        collector.set_book_genre('11/22/63', 'Фантастика')
        assert collector.get_book_genre('11/22/63') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('11/22/63')
        collector.set_book_genre('11/22/63', 'Роман')
        assert collector.get_book_genre('11/22/63') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Цитаты Камы Пули')
        collector.set_book_genre('Цитаты Камы Пули', 'Фантастика')
        collector.add_new_book('Ты не бойся ночи ведь я рядом')
        collector.set_book_genre('Ты не бойся ночи ведь я рядом', 'Ужасы')
        collector.add_new_book('Большая зарплата')
        collector.set_book_genre('Большая зарплата', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Цитаты Камы Пули', 'Большая зарплата']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Цитаты Камы Пули')
        collector.set_book_genre('Цитаты Камы Пули', 'Фантастика')
        collector.add_new_book('Ты не бойся ночи ведь я рядом')
        collector.set_book_genre('Ты не бойся ночи ведь я рядом', 'Ужасы')
        collector.add_new_book('Большая зарплата')
        collector.set_book_genre('Большая зарплата', 'Фантастика')
        assert collector.get_books_for_children() == ['Цитаты Камы Пули', 'Большая зарплата']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цитаты Камы Пули')
        collector.add_book_in_favorites('Цитаты Камы Пули')
        assert collector.get_list_of_favorites_books() == ['Цитаты Камы Пули']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цитаты Камы Пули')
        collector.add_book_in_favorites('Цитаты Камы Пули')
        collector.delete_book_from_favorites('Цитаты Камы Пули')
        assert collector.get_list_of_favorites_books() == []