import json

def show_menu():
    print("\nМеню:")
    print("1. Показать все книги")
    print("2. Добавить книгу")
    print("3. Найти книгу по автору")
    print("4. Удалить книгу")
    print("5. Изменить статус книги")
    print("6. Выход\n")

def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def print_books_mini(books):
    for book in books:
        print(f'{book["id"]}. {book["name"]} — {book["author"]} ({book["year"]})')

def print_books_maxi(books):
    for book in books:
        print(f'{book["id"]}. {book["name"]} — {book["author"]} ({book["year"]}). '
              f'{book["genre"]}, {book["status"].lower()}, рейтинг: {book["rating"]} ⭐')

def print_book(book):
    print(f'{book["id"]}. {book["name"]} — {book["author"]} ({book["year"]}). '
          f'{book["genre"]}, {book["status"].lower()}, рейтинг: {book["rating"]} ⭐')

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите число!")

def get_next_id(books):
    if not books:
        return 1
    return max(book["id"] for book in books) + 1

def add_book(books):
    new_book = {
        "id": get_next_id(books),
        "name": input("Введите название книги: "),
        "author": input("Введите автора: "),
        "genre": input("Введите жанр: "),
        "year": input_int("Введите год: "),
        "status": input("Введите статус: "),
        "rating": input("Введите рейтинг: ")
    }
    books.append(new_book)

def find_books_by_author(books):
    auth = input("Введите автора: ").lower()
    found = False

    for book in books:
        if book["author"].lower() == auth:
            print_book(book)
            found = True

    return found

def delete_book_by_name(books):
    name = input("Введите название: ").lower()
    new_books = [book for book in books if book["name"].lower() != name]
    return new_books, len(new_books) != len(books)

def delete_book_by_id(books):
    book_id = input_int("Введите id: ")
    new_books = [book for book in books if book["id"] != book_id]
    return new_books, len(new_books) != len(books)

# ✅ исправлено: поиск + found + возврат
def change_book_by_name(books):
    name = input("Введите название: ").lower()
    found = False

    for book in books:
        if book["name"].lower() == name:
            book["status"] = input("Введите новый статус: ")
            book["rating"] = input("Введите новый рейтинг: ")
            print("Книга обновлена:")
            print_book(book)
            found = True

    return found

# ✅ исправлено: found + возврат
def change_book_by_id(books):
    book_id = input_int("Введите id: ")
    found = False

    for book in books:
        if book["id"] == book_id:
            book["status"] = input("Введите новый статус: ")
            book["rating"] = input("Введите новый рейтинг: ")
            print("Книга обновлена:")
            print_book(book)
            found = True

    return found


books = load_books()

while True:
    show_menu()

    try:
        n = int(input("Выберите действие: "))
    except ValueError:
        print("Введите число!")
        continue

    if n == 1:
        if not books:
            print("Библиотека пуста")
        else:
            print_books_maxi(books)

    elif n == 2:
        add_book(books)
        save_books(books)
        print("Книга добавлена!")
        print("\nТекущая библиотека:")
        print_books_mini(books)

    elif n == 3:
        found = find_books_by_author(books)
        if not found:
            print("Книги не найдены")

    elif n == 4:
        print("1 — удалить по названию")
        print("2 — удалить по id")

        try:
            num = int(input("Выберите способ: "))
        except ValueError:
            print("Ошибка ввода")
            continue

        if num == 1:
            books, deleted = delete_book_by_name(books)
        elif num == 2:
            books, deleted = delete_book_by_id(books)
        else:
            print("Неверный выбор")
            continue

        if deleted:
            save_books(books)
            print("Книга удалена")
            print("\nОбновлённая библиотека:")
            print_books_mini(books)
        else:
            print("Книга не найдена")

    elif n == 5:
        print("1 — изменить по названию")
        print("2 — изменить по id")

        try:
            num = int(input("Выберите способ: "))
        except ValueError:
            print("Ошибка ввода")
            continue

        if num == 1:
            found = change_book_by_name(books)
        elif num == 2:
            found = change_book_by_id(books)
        else:
            print("Неверный выбор")
            continue

        if found:
            save_books(books)
        else:
            print("Книга не найдена")

    elif n == 6:
        print("Пока!")
        break

    else:
        print("Нет такого пункта меню")