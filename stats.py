def get_num_words(str):
        return  len(str.split())

def get_character_frequency(text):
	dict = {}
	for char in text:
		char = char.lower()
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] = dict[char] + 1
	return dict
