from stats import count_words


#read the book content:
def get_book_text(file_path):
  book_content = ""
  with open(file_path) as f:
    book_content = f.read()
  return book_content


print(count_words(get_book_text("books/frankenstein.txt")))