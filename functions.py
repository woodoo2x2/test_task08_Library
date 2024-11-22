from classes import Library, Book
def main():
    library = Library()

    while True:
        print("\nБиблиотека - Меню")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)
            print(f"Книга '{title}' добавлена!")

        elif choice == "2":
            id = int(input("Введите номер книги, которую хотите удалить: "))
            library.delete_book_by_id(id)
            print(f"Книга с номером {id} удалена!")

        elif choice == "3":
            print("\n1. Поиск по номеру")
            print("2. Поиск по названию")
            print("2. Поиск по автору")
            choice = input("Выберите действие: ")
            # keyword = input("Введите ключевое слово для поиска: ")
            # results = library.search_books(keyword)
            if choice == '1':
                id = int(input('Введите номер книги'))
                book = library.find_book_by_id(id)
                print(f"Номер книги: {book['id']}\nНазвание: {book['title']}\nАвтор: {book['author']}\nГод: {book['year']}\nВ наличии : {'Да' if book['status'] else 'Нет'}\n")
            # if results:
            #     print("Найденные книги:")
            #     for book in results:
            #         print(f"Название: {book.title}\n Автор: {book.author}\n Год: {book.year}\n ISBN: {book.isbn}")
            # else:
            #     print("Книг по вашему запросу не найдено.")

        elif choice == "4":
            books = library.show_all_books()
            if books:
                print("Все книги в библиотеке:\n ")
                for book in books:
                    print(f"Номер книги: {book['id']}\nНазвание: {book['title']}\nАвтор: {book['author']}\nГод: {book['year']}\nВ наличии : {'Да' if book['status'] else 'Нет'}\n")
            else:
                print("Библиотека пуста.")

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")