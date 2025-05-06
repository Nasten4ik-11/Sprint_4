import pytest

from main import BooksCollector

# 1. Проверка добавления книги
def test_add_new_book_adds_book_to_list():
    collector = BooksCollector()
    collector.add_new_book("Мастер и Маргарита")
    assert "Мастер и Маргарита" in collector.get_books_genre()

# 2. Проверка установки жанра
def test_set_book_genre_assigns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book("Мастер и Маргарита")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

# 3. Проверка получения жанра книги
def test_get_book_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book("Мастер и Маргарита")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    genre = collector.get_book_genre("Мастер и Маргарита")
    assert genre == "Фантастика"

# 4. Книга с возрастным жанром не попадает в список для детей
def test_get_books_for_children_excludes_adult_genres():
    collector = BooksCollector()
    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")
    assert "Оно" not in collector.get_books_for_children()

# 5. Проверка списка книг с определённым жанром
def test_get_books_with_specific_genre_returns_expected_list():
    collector = BooksCollector()
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    result = collector.get_books_with_specific_genre("Детективы")
    assert "Шерлок Холмс" in result

# 6. Проверка добавления книги в избранное
def test_add_favorites_adds_book_to_favorites_list():
    collector = BooksCollector()
    collector.add_new_book("Винни-Пух")
    collector.add_book_in_favorites("Винни-Пух")
    assert "Винни-Пух" in collector.get_list_of_favorites_books()

# 7. Проверка удаления книги из избранного
def test_delete_book_from_favorites_removes_book():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

# 8. Проверка возврата списка избранных книг
def test_get_list_of_favorites_returns_only_favorites():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.add_book_in_favorites("Книга 2")
    assert collector.get_list_of_favorites_books() == ["Книга 2"]

# 9. Книга без жанра возвращает None
def test_add_new_book_without_genre_returns_none():
    collector = BooksCollector()
    collector.add_new_book("Неизвестная книга")
    assert collector.get_book_genre("Неизвестная книга") == ''

# 10. Параметризованный тест для добавления книг
@pytest.mark.parametrize("book_name", ["Книга A", "Книга B", "Книга C"])
def test_add_multiple_books(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()



# 11. Проверка длины, больше 40 символов
def test_add_new_book_does_not_add_if_name_too_long():
    collector = BooksCollector()
    long_title = "Очень длинное название книги, которое превышает 40 символов"
    collector.add_new_book(long_title)
    assert long_title not in collector.get_books_genre()

