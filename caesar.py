import os
import random

class Caesar:
    def __init__(self, file_name):
        self.characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.big_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.special_characters = [' ','@', '#', '$', '%', '&', '*', '(', ')', '_', '!', '^', '-', '+', ',']

        self.cesar_sentences = []
        self.key = []

        self.sentences = self.FileRead(file_name)
        self.Menu()

    def FileRead(self, file_name):
        file = []
        with open(file_name, 'r') as f:
            for line in f:
                if line.strip() != "": 
                    file.append(line.strip())
        return file
    
    def Menu(self):
        flaga = True
        self.cesar_sentences = []
        self.key = []

        while flaga:
            mode = 0
            os.system('cls')
            print("--- Caesar cipher ---")
            print("1. Encryption")
            print("2. Decryption") 
            print("3. Exit") 
            mode = int(input("Specify the operation of the programme (only number): "))
            match mode:
                case 1:
                    print("1")
                    flaga = False
                    self.Menu2(mode)
                case 2:
                    print("2")
                    flaga = False
                    self.Menu2(mode)
                case 3:
                    os.system('cls')
                    flaga = False
                    print("Thank you for using my program!")
                case _:
                    flaga = True

    def Menu2(self, mode_in):
        flaga = True
        while flaga:
            mode = 0
            os.system('cls')
            print("--- Caesar cipher - code in file ---")
            print("1. Default shift - 3")
            print("2. Enter shift") 
            match mode_in:
                case 1:
                    print("3. Random shift (key)")
                case 2:
                    print("3. Drawn shift (key)")
            print("4. Back") 
            mode = int(input("Specify the operation of the programme (only number): "))
            match mode:
                case 1:
                    flaga = False
                    self.Cipher((mode_in*3 + mode-1)-2)
                case 2:
                    flaga = False
                    self.Cipher((mode_in*3 + mode-1)-2)
                case 3:
                    flaga = False
                    self.Cipher((mode_in*3 + mode-1)-2)
                case 4:
                    flaga = False
                    self.Menu()
                case _:
                    flaga = True

    def Cipher(self, mode_in):
        match mode_in:
            # Encryption
            case 1:
                self.key = self.Key(3)
            case 2:
                self.key = self.Key(int(input("Enter the shift: ")))
            case 3:
                self.key = self.RandomKey()
                print("Generated key:")
                print(self.key)
            # Decryption
            case 4:
                self.key = self.Key(-3)
            case 5:
                self.key = self.Key((int(input("Enter the shift: ")))*-1)
            case 6:
                key_str = input("Enter key, comma-separated 36 numbers: ")
                key_list = key_str.split(',')
                self.key = [int(x.strip())*-1 for x in key_list]

        self.cesar_sentences = self.CipherChange(self.sentences, self.key)
        self.Output()


    def Key(self, shift):
        key = []
        for _ in range(36):
            key.append(shift)
        return key

    def RandomKey(self):
        key = list(range(1, 37))
        random.shuffle(key)
        return key

    def CipherChange(self, words, key):
        cesar_sentences_out = []
        for sentence in words:
            cesar_sentence = ''
            for letter, char in zip(sentence, key):
                special_character = False
                for i in range(len(self.special_characters)):
                    if letter == self.special_characters[i]:
                        cesar_sentence += self.special_characters[i]
                        special_character = True
                if special_character == False:
                    index = self.characters.index(letter.lower()) if letter.lower() in self.characters else self.big_characters.index(letter)
                    shift = (index + char) % 36
                    cesar_sentence += self.big_characters[shift]
            cesar_sentences_out.append(cesar_sentence)
        return cesar_sentences_out

    def Output(self):
        print("Input: {}".format(self.sentences))
        print("Output: {}".format(self.cesar_sentences))

def main():
    file1 = Caesar("text.txt")

if __name__ == "__main__":
    main()
