from stats import get_num_words
from stats import get_character_frequency
from stats import sort_dict
import sys
import os

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main(book_file):
	print("============ BOOKBOT ============")
	
	print(f"Analyzing book found at {book_file}...")
	text = get_book_text(book_file)
	
	print("----------- Word Count ----------")
	word_count = get_num_words(text)
	print(f'Found {word_count} total words')

	print("--------- Character Count -------")
	char_frequency = get_character_frequency(text)
	char_list = sort_dict(char_frequency)
	[print(f'{c['char']}: {c['num']}') for c in char_list if c["char"].isalpha()]
	
	print("============= END ===============")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	if os.path.exists(sys.argv[1]):
		main(sys.argv[1])
	else:
		print("File not found")
		sys.exit(2)
