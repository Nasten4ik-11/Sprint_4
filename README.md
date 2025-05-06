# Проект Sprint 4: BooksCollector

## Реализованные тесты:

1. test_add_new_book_adds_book_to_list — проверяет, что книга добавляется в список.
2. test_set_book_genre_assigns_correct_genre — проверяет, что жанр книги устанавливается правильно.
3. test_get_book_genre_returns_correct_genre — проверяет, что метод возвращает установленный жанр.
4. test_get_books_for_children_excludes_adult_genres — проверяет, что книги с возрастными жанрами не попадают в список для детей.
5. test_get_books_with_specific_genre_returns_expected_list — проверяет выборку книг по жанру.
6. test_add_favorites_adds_book_to_favorites_list — проверяет добавление книги в избранное.
7. test_delete_book_from_favorites_removes_book — проверяет удаление книги из избранного.
8. test_get_list_of_favorites_returns_only_favorites — проверяет список избранных книг.
9. test_add_new_book_without_genre_returns_none — проверяет, что у книги без жанра метод возвращает None.
10. Параметризованные тесты — применяются для повторяющихся сценариев (например, добавление нескольких книг с разными названиями).

---

## Запуск тестов

```bash
pytest -v tests.pyS