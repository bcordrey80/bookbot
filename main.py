import sys
from stats import get_num_words, get_num_characters, get_sorted_characters

def main():
	if len(sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	total_words = get_num_words(sys.argv[1])
	sorted_chars = get_sorted_characters(sys.argv[1])

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(total_words)
	print("--------- Character Count -------")
	for item in sorted_chars:
		print(f"{item["char"]}: {item["num"]}")

main()