class Palyndrome:
    def __init__(self, word):
        self.word = word
    def estPalyndrome(self):
        word = self.word.lower()
        return word == word[::-1]

def main():
    sentence = input("enter a word pls: ")
    word = Palyndrome(sentence)
    print(word.estPalyndrome())
if __name__=="__main__":
    main()