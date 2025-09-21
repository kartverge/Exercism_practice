"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    prefix = 'un'
    return prefix + word
   


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return f'{prefix} :: {" :: ".join(prefixed_words)}'
    


def remove_suffix_ness(word):
    if word.endswith('iness'):
        new_word = word[:-5]+'y'
        return new_word
    elif word.endswith('ness'):
        new_word2 = word[:-4]
        return new_word2
    else:
        return word

   

  

def adjective_to_verb(sentence, index):
    list = sentence.split()
    word_needed = list[index]
    if "." in word_needed:
        word_needed_wthoutpun = word_needed[:-1] + "en"
        return word_needed_wthoutpun
    else:
        return word_needed + "en"
        word_needed
        
