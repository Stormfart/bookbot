def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
    return content

def word_count(text):
  wc_list = text.split()
  return len(wc_list)

def main():
  book = get_book_text("books/frankenstein.txt")
  wc = word_count(book)
  print(f"Found {wc} total words")

if __name__ == '__main__':
  main()