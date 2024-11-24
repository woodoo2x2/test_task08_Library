from classes import Library
def show_books_info(books: list) -> None:
    """Показывает информацию о списке книг."""
    if books:
        for book in books:
            print(
                f"Номер книги: {book['id']}\nНазвание: {book['title']}\nАвтор: {book['author']}\nГод: {book['year']}\nВ наличии : {'Да' if book['status'] else 'Нет'}\n")
    else:
        print("Книг не найдено.")


def search_books(library: Library) -> None:
    """Предоставляет возможность поиска книг."""
    print("\n1. Поиск по году написания")
    print("2. Поиск по названию")
    print("3. Поиск по автору")

    choice = input("Выберите действие: ")

    if choice == '1':
        year = int(input('Введите год написания книги: '))
        books = library.find_book_by_year(year)
        show_books_info(books)

    elif choice == '2':
        title = input('Введите название книги: ')
        book = library.find_book_by_title(title)
        if book:
            show_books_info([book])
        else:
            print(f'Книги с названием "{title}" нет в библиотеке.')

    elif choice == "3":
        author = input('Введите автора: ')
        books = library.find_book_by_author(author)
        show_books_info(books)


def main() -> None:
    library = Library()

    actions = {
        "1": lambda: add_book(library),
        "2": lambda: delete_book(library),
        "3": lambda: search_books(library),
        "4": lambda: show_all_books(library),
        "5": lambda: change_book_status(library),
        "6": lambda: exit_program()
    }

    while True:
        print("\nБиблиотека - Меню")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


def add_book(library: Library) -> None:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания книги: "))
    library.add_book(title, author, year)
    print(f"Книга '{title}' добавлена!")


def delete_book(library: Library) -> None:
    book_id = int(input("Введите номер книги, которую хотите удалить: "))
    library.delete_book_by_id(book_id)
    print(f"Книга с номером {book_id} удалена!")


def show_all_books(library: Library) -> None:
    books = library.show_all_books()
    show_books_info(books)


def change_book_status(library: Library) -> None:
    book_id = int(input("Введите номер книги, статус которой вы хотите изменить: "))
    book = library.find_book_by_id(book_id)
    if book:
        library.change_book_status_by_id(book_id)
        print(f'Статус книги "{book["title"]}" изменен. Статус: {"Да" if book["status"] else "Нет"}')
    else:
        print('Книги с таким номером нет в библиотеке')


def exit_program() -> None:
    print("Выход из программы. До свидания!")
    exit()


if __name__ == "__main__":
    main()