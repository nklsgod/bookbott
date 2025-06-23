def count_words(book):
  word_list = []
  word_list = book.split()
  for word in word_list:
    if word == " ":
      word_list.remove(word)
  word_count = len(word_list)
  return f"{word_count} words found in the document"