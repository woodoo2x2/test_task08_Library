import unittest
import os
import json
from classes import Library, Book

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.library = Library('test_library.json')
        # Создаем тестовый файл filename
        self.test_file = 'test_library.json'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    def tearDown(self):
        """Очистка после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("1984", "George Orwell", 1949)
        books = self.library.show_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "1984")
        self.assertEqual(books[0]['author'], "George Orwell")

    def test_delete_book_by_id(self):
        """Тест удаления книги."""
        self.library.add_book("1984", "George Orwell", 1949)
        self.library.delete_book_by_id(1)
        books = self.library.show_all_books()
        self.assertEqual(len(books), 0)


    def test_find_book_by_id(self):
        """Тест поиска книги по ID."""
        self.library.add_book("1984", "George Orwell", 1949)
        book = self.library.find_book_by_id(1)
        self.assertEqual(book['title'], "1984")
        self.assertEqual(book['author'], "George Orwell")

    def test_find_nonexistent_book_by_id(self):
        """Тест поиска несуществующей книги по ID."""
        book = self.library.find_book_by_id(99)
        self.assertEqual(book, None)

    def test_show_all_books(self):
        """Тест отображения всех книг."""
        self.library.add_book("1984", "George Orwell", 1949)
        self.library.add_book("Animal Farm", "George Orwell", 1945)
        books = self.library.show_all_books()
        self.assertEqual(len(books), 2)

    def test_find_book_by_title(self):
        """Тест поиска книги по названию."""
        self.library.add_book("1984", "George Orwell", 1949)
        book = self.library.find_book_by_title("1984")
        self.assertEqual(book['author'], "George Orwell")

    def test_find_nonexistent_book_by_title(self):
        """Тест поиска книги с несуществующим названием."""
        book = self.library.find_book_by_title("Nonexistent Book")
        self.assertEqual(book, None)

if __name__ == "__main__":
    unittest.main()