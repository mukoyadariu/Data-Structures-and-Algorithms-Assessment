import string

def word_frequency(sentence):
    
    words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    freq_dict = {}
    
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    

    return freq_dict

# Test cases
sentence_1 = "Hello, world! Hello, Python!"
result_1 = word_frequency(sentence_1)
print(result_1)  

sentence_2 = "The quick brown fox jumps over the lazy dog."
result_2 = word_frequency(sentence_2)
print(result_2)  

sentence_3 = "To be or not to be, that is the question."
result_3 = word_frequency(sentence_3)
print(result_3)  