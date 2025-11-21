import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', [
        'Мастер и Маргарита',
        'Незнайка на Луне', 
        'Тайна третьей планеты',
        'Война и мир'
    ])
    def test_add_new_book_appears_in_dict(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', [
        '',
        'Очень длинное название книги которое превышает лимит в 40 символов',
    ])
    def test_add_new_book_invalid_name_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('book_name, genre', [
        ('Незнайка на Луне', 'Фантастика'),
        ('Тайна третьей планеты', 'Фантастика'),
        ('Каникулы в Простоквашино', 'Мультфильмы'),
        ('Смешарики', 'Комедии')
    ])
    def test_set_book_genre_correctly_set(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('invalid_genre', [
        'Роман',
        'Драма',
        'Поэзия',
        'Приключения'
    ])
    def test_set_book_genre_invalid_not_set(self, invalid_genre):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', invalid_genre)
        assert collector.get_book_genre('Мастер и Маргарита') == ''

    @pytest.mark.parametrize('book_name, genre', [
        ('Незнайка на Луне', 'Мультфильмы'),
        ('Тайна третьей планеты', 'Фантастика'),
        ('Смешарики', 'Комедии')
    ])
    def test_get_books_by_genre_returns_correct(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book_name in books

    @pytest.mark.parametrize('book_name, genre', [
        ('Ночной дозор', 'Ужасы'),
        ('Дело пестрых', 'Детективы')
    ])
    def test_get_books_for_children_excludes_adult(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()
        assert book_name not in children_books

    def test_add_book_to_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна третьей планеты')
        collector.add_book_in_favorites('Тайна третьей планеты')
        collector.delete_book_from_favorites('Тайна третьей планеты')
        assert 'Тайна третьей планеты' not in collector.get_list_of_favorites_books()

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        assert isinstance(collector.get_books_genre(), dict)
        