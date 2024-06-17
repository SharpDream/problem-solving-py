def even_word(word):
    print(f"Orginal String is '{word}'")
    print("Printing only even index chars")

    letter_list = []
    for letter in word:
        letter_list.append(letter)

    for len_list in range(len(letter_list)):
        if len_list % 2 == 0:
            for new_letter in letter_list[len_list]:
                print(new_letter)
        else:
            pass


even_word("PYnative")
