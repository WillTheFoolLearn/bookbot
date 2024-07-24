def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        words = file_contents.split()
        print(len(words), "words found in the document\n")
        letters = {}

        for word in words:
            for letter in word.lower():

                if letter in letters:
                    letters[letter] += 1
                elif letter.isalpha():
                    letters[letter] = 1
        
        ordered_letters = dict(sorted(letters.items(), key=lambda x:x[1], reverse = True))

        for letter in ordered_letters:
            print(f"The {letter} character was found {ordered_letters[letter]} times")
        
    print("--- End report ---")

main()