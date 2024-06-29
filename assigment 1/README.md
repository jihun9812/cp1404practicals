
# Books to Read 1.0

This is a simple program to keep track of books you want to read and books you have finished. The program lets you see all books, add a new book, and mark a book as finished. The list of books is stored in a CSV file.

## Features

- Show all books, sorted by author and title
- Add a new book with title, author, and number of pages
- Mark a book as finished
- Save the book list to a CSV file

## How to Use

1. **Download the code**:
   - Clone the repository or download the zip file from GitHub.
   - Open the folder in your computer.

2. **Make sure the `books.csv` file is in the same folder as `assignment1.py`**:
   The `books.csv` file should have the following books:
   ```csv
   Developing the Leader Within You,John Maxwell,225,u
   The 360 Degree Leader,John Maxwell,369,c
   In Search of Lost Time,Marcel Proust,93,u
   Starting Out with Python,Tony Gaddis,744,c
   ```

3. **Run the program**:
   - Open a terminal or command prompt.
   - Go to the folder where the files are located.
   - Run the program with the command:
     ```sh
     python assignment1.py
     ```

4. **Menu options**:
   - `D`: Show all books
   - `A`: Add a new book
   - `C`: Mark a book as finished
   - `Q`: Quit the program

## Example

Here is an example of how the program works:

```
Books to Read 1.0 by [Your Name]
4 books loaded.
Menu:
D - Show all books
A - Add a new book
C - Mark a book as finished
Q - Quit
>>> D
*1. Developing the Leader Within You by John Maxwell   225 pages
 2. The 360 Degree Leader            by John Maxwell   369 pages
*3. In Search of Lost Time           by Marcel Proust   93 pages
 4. Starting Out with Python         by Tony Gaddis    744 pages
You still need to read 318 pages in 2 books.
```

## Author

[Your Name]
