def translate(sentence, translator):
    return translator(sentence)

def yoda(sentence):
    words = sentence.split()
    middle = len(words) // 2
    new_sentence = " ".join(words[middle:] + words[:middle])
    return new_sentence

def gungan(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        if i % 4 == 0:
            word[i] = word + "sa"
    new_sentence = " ".join(words) + ", sa!"
    return new_sentence

if __name__ == "__main__":
    while True:
        try:
            print()
            sentence = input(" Enter a sentence to translate, or enter 'Q' to quit: ")
            if sentence == "Q":
                break
            print()
            print("Choose which translator to use: ")
            print(" 1) Yoda     2) Gungan")
            print()
            choice = input("Enter your choice: ")
            print()
            if choice == "1":
                print(translate(sentence, yoda))
            elif choice == "2":
                print(translate(sentence, gungan))
            else:
                print("Invalid choice. Please try again.")
                
            print()
                
        except Exception as e:
            print(f"Error: {e}")