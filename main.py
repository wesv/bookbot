from stats import get_num_words
from stats import get_character_frequency
from stats import sort_dict

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main():
	print("============ BOOKBOT ============")
	
	print("Analyzing book found at books/frankenstein.txt...")
	text = get_book_text("books/frankenstein.txt")
	
	print("----------- Word Count ----------")
	word_count = get_num_words(text)
	print(f'Found {word_count} total words')

	print("--------- Character Count -------")
	char_frequency = get_character_frequency(text)
	char_list = sort_dict(char_frequency)
	[print(f'{c['char']}: {c['num']}') for c in char_list if c["char"].isalpha()]
	
	print("============= END ===============")

if __name__ == "__main__":
	main()
