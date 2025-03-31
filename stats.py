def get_book_text(filename):
        with open(filename) as f:
                filename = f.read()
        return filename

def get_num_words(text):
        count = 0
        words = text.split()
        for word in words:
                count += 1
        return count

def get_letter_count(text):
	text = text.lower()
	characters = {}
	for character in text:
		if character in characters:
			characters[character] += 1
		else:
			characters[character] = 1
	return characters

def sort_on(split_dictionary):
	return split_dictionary["num"]

def get_sorted_list(characters):
	split_dictionary = []
	sorted_dict = []
	for character, count in characters.items():
		split_dictionary.append({"name": character, "num": count})
	split_dictionary.sort(reverse=True, key=sort_on)

	return split_dictionary
