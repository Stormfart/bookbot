import sys
from stats import word_count
from stats import character_count
from stats import sort_count

def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
    return content

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book = get_book_text(sys.argv[1])
  wc = word_count(book)
  cc = character_count(book)
  sc = sort_count(cc)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {wc} total words")
  print("--------- Character Count -------")
  for i in sc:
    print(f"{i['char']}: {i['num']}")
  print("============= END ===============")

if __name__ == '__main__':
  main()