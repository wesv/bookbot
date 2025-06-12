from stats import get_num_words
from stats import get_character_frequency

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main():
	text = get_book_text("books/frankenstein.txt")
	print(f'{get_num_words(text)} words found in the document')
	char_frequency = get_character_frequency(text)
	print(f'{char_frequency}')

if __name__ == "__main__":
	main()
