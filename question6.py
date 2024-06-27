# Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
# for his unique way of speaking. He often reverses the order of words in his
# sentences. For example, instead of saying "I am home" he might say "Home
# am I" Design a function that takes a sentence as input and returns a new
# sentence with the words reversed in the same order that Master Yoda would
# use.

def reverse_words(sentence):
    """This function takes a sentence,
    reverses the words in it and returns it
    
    Args:
        sentence (str): The string to be reversed
    
    Returns (str): The sentence in reversed order
    """
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence

#testing
sentence = "My name is Jenny"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence) #Output: "Jenny is name my"