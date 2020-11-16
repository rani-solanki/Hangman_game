import string
import random
def load_words():
    ghtr="words.txt"
    word_list=open(ghtr,"r")
    line=word_list.readline()
    word_list = str.split(line)
    print ("  ", len(word_list), "words loaded.\n")
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
    print(secret_word)
