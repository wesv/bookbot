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


def sort(dict):
        return dict["num"]

def sort_dict(dictionary):
	sorted = [{"char":key, "num":dictionary[key]} for key in dictionary]
	sorted.sort(reverse=True, key=sort)
	return sorted
