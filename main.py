def num_words(str):
	return  len(str.split())

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main():
	print(f'{num_words(get_book_text("books/frankenstein.txt"))} words found in the document')
	#print(num_words("Hello my test"))

if __name__ == "__main__":
	main()
