from stats import word_count
from stats import character_count

def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
    return content

def main():
  book = get_book_text("books/frankenstein.txt")
  wc = word_count(book)
  cc = character_count(book)
  print(f"Found {wc} total words")
  print(cc)

if __name__ == '__main__':
  main()