import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_letter_count
from stats import get_sorted_list

def main():
	if len(sys.argv) < 2: 
		print( "Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_text = sys.argv[1]
	text = get_book_text(book_text)
	num_words = get_num_words(text)
	total_characters = get_letter_count(text)
	amount_of_characters = get_sorted_list(total_characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_text}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in amount_of_characters:
		if item['name'].isalpha():
			print(f"{item['name']}: {item['num']}")
	print("============= END ===============")
	
main()
