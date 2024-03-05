file_path = "text.txt"
shift = 2

sentences = []
cesar_sentences = []

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

big_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


with open(file_path, 'r') as f:
    for line in f:
        if line.strip() != "": 
            sentences.append(line.strip())

for sentence in range(len(sentences)):
    cesar_sentence = ''
    for letter in range(len(sentences[sentence])):
        for character in range(len(characters)):
            if characters[character] == sentences[sentence][letter] or big_characters[character] == sentences[sentence][letter]:
                cesar_sentence += big_characters[character + shift]
    cesar_sentences.append(cesar_sentence)

print(cesar_sentences)
            




            

