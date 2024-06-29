
"""
Name: [jihun kim]
Date: [01/07/2024]
GitHub URL: [https://github.com/CP1404/a1-jihun9812]
"""


FILENAME = 'books.csv'
COMPLETED = 'c'
UNREAD = 'u'

def load_books(filename):
    """csv file to list"""
    books = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                parts[2] = int(parts[2])  # 페이지 수를 정수로 변환
                books.append(parts)
        file.close()
        print(f"{len(books)} books loaded from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Starting with an empty list.")
    return books

def save_books(books, filename):
    """리스트의 책 데이터를 CSV 파일에 저장"""
    file = open(filename, 'w')
    for book in books:
        line = ','.join([book[0], book[1], str(book[2]), book[3]])
        file.write(line + '\n')
    file.close()
    print(f"{len(books)} books saved to {filename}")

def display_books(books):
    """책 목록을 깔끔하게 정렬하여 표시"""
    books.sort(key=lambda x: (x[1], x[0]))  #
    unread_count = 0
    total_pages = 0

    for i, book in enumerate(books):
        status = '*' if book[3] == UNREAD else ' '
        print(f"{status}{i + 1}. {book[0]:<30} by {book[1]:<20} {book[2]} pages")
        if book[3] == UNREAD:
            unread_count += 1
            total_pages += book[2]

    print(f"You still need to read {total_pages} pages in {unread_count} books.")

def add_book(books):
    """새 책을 추가하는 함수"""
    title = input("Title: ").strip()
    while not title:
        print("Input can not be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while not author:
        print("Input can not be blank")
        author = input("Author: ").strip()

    pages = input("Number of Pages: ").strip()
    while not pages.isdigit() or int(pages) <= 0:
        print("Invalid input - please enter a valid number")
        pages = input("Number of Pages: ").strip()

    books.append([title, author, int(pages), UNREAD])
    print(f"{title} by {author} ({pages} pages) added.")

def complete_book(books):
    """책을 완료로 표시하는 함수"""
    display_books(books)
    if all(book[3] == COMPLETED for book in books):
        print("No unread books - well done!")
        return

    book_number = input("Enter the number of a book to mark as completed: ").strip()
    while not book_number.isdigit() or not (1 <= int(book_number) <= len(books)):
        print("Invalid input - please enter a valid number")
        book_number = input("Enter the number of a book to mark as completed: ").strip()

    book_number = int(book_number)
    if books[book_number - 1][3] == COMPLETED:
        print("That book is already completed")
    else:
        books[book_number - 1][3] = COMPLETED
        print(f"{books[book_number - 1][0]} by {books[book_number - 1][1]} completed!")

def main():
    """메인 함수"""
    print("Books to Read 1.0 by [jihun kim]")
    books = load_books(FILENAME)

    menu = """
Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
"""
    while True:
        choice = input(menu).strip().upper()
        if choice == 'D':
            display_books(books)
        elif choice == 'A':
            add_book(books)
        elif choice == 'C':
            complete_book(books)
        elif choice == 'Q':
            save_books(books, FILENAME)
            print("So many books, so little time. Frank Zappa")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()
