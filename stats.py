def get_book_text(filepath):
	file_contents = ""
	with open(filepath) as file:
		file_contents = file.read()
	return file_contents

def get_num_words(filepath):
	file_contents = get_book_text(filepath).split()
	return f"Found {len(file_contents)} total words"

def get_num_characters(filepath):
	result = {}
	file_contents = get_book_text(filepath).split()
	for word in file_contents:
		word = word.lower()
		for character in word:
			if character in result:
				result[character] += 1
			else:
				result[character] = 1
	return result

def get_sorted_characters(filepath):
	num_characters = get_num_characters(filepath)
	new_counts = []
	for item in num_characters:
		if item.isalpha():
			new_counts.append({"char": f"{item}", "num": f"{num_characters[item]}"})
	sorted_counts = sorted(new_counts, key=lambda d: int(d['num']), reverse=True)
	return sorted_counts
