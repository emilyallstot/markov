import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    file = open(corpus)
    markov_dictionary = {}
    word_key = ['None', 'None']
    word_list = []

#use for loop to make lines in file a list
    for line in file:
        line = line.strip()
        words = line.split(" ")

        # generate keys

        word_key[0] = words[len(words)-1]
        word_key[1] = words[0]
        
        #markov_dictionary[tuple(word_key)] = make_values(corpus, word_key)
        markov_dictionary[tuple(word_key)] = []

        i = 0
        while i < len(words) - 1:
            word_key[0] = words[i]
            word_key[1] = words[i + 1]
            #markov_dictionary[tuple(word_key)] = make_values(corpus, word_key)
            markov_dictionary[tuple(word_key)] = []

            i += 1
    return markov_dictionary

print make_chains("green-eggs.txt")


def make_values(corpus, word_key):
    
    values_list = []
    
    file = open(corpus)

    for line in file:
        line = line.strip()
        words = line.split(" ")
        
        i = 0
        while i < len(words) - 2:
            if word_key[0] == words[i]:
                if word_key[1] == words[i + 1]:
                    values_list.append(words[i + 2])
            

            i += 1

    return values_list

print('\n')
print make_values("green-eggs.txt", ('you', 'like'))


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# make_chains('green-eggs.txt')


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
